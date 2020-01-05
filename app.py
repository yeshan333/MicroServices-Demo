# -*- utf-8 -*-

import json
import sqlite3
import sys
import random

from flask import Flask, jsonify, make_response, request, abort, render_template, redirect, url_for
from flask import session
from flask_cors import CORS, cross_origin
from time import strftime, gmtime
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'  # session config


CORS(app)

# CROSS-ORIGIN-RESOURCE-SHARING
cors = CORS(app, resources={r"/api/*": {"origin": "*"}})

connection = MongoClient("mongodb://localhost:27017/")

def create_mongodatabase():
    try:
        dbnames = connection.list_database_names()
        if 'cloud_native' not in dbnames:
            db = connection.cloud_native.users
            db_tweets = connection.cloud_native.tweets
            db_api = connection.cloud_native.apirelease
            db.insert_one({
                "email": "1329441308@qq.com",
                "id": 33,
                "name": "yeshan",
                "password": "123456",
                "username": "Cloudys"
            })

            db_tweets.insert_one({
                "body": "Happy New Year!",
                "id": 18,
                "timestamp": "2020-01-01T00:00:00Z",
                "tweetedby": "Cloudys"
            })

            db_api.insert_one({
                "buildtime": "2020-01-01 00:00:00",
                "links": "api/v1/users",
                "methods": "get,post",
                "version": "v1"
            })

            db_api.insert_one({
                "buildtime": "2020-01-01 10:01:00",
                "links": "api/v1/users",
                "methods": "get,post",
                "version": "v2"
            })
            print("Database Initialize completed!")
        else:
            print("Database already Initialized!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Database creation failed!")

# get api information
@app.route('/api/v1/info')
def home_index():
    db = connection.cloud_native.apirelease
    print('Open Database Sucessful !')
    api_list = []
    for row in db.find():
        api_list.append(str(row))
    return jsonify({'api_version': api_list}), 200

# get all user information
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()

def list_users():
    db = connection.cloud_native.users
    print('Open Database Sucessful!')
    user_list = []

    for i in db.find():
        # print(type(i)) # i is a python dict
        user_list.append(str(i))
    if user_list == []:
        abort(404)

    return jsonify({'user_list':user_list})

# get user information
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return list_user(user_id)

def list_user(user_id):
    db = connection.cloud_native.users
    print('Open Database Sucessful!')
    user_list = []

    for i in db.find({"id": user_id}):
        # print(type(i)) # i is a python dict
        user_list.append(str(i))
    if user_list == []:
        abort(404)

    return jsonify({'user_list':user_list})

@app.errorhandler(404)
def resource_not_found(error):
    return make_response({'error':'Resource not found!'}, 404)

# post user information
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json or \
        not 'email' in request.json or not 'password' in request.json:
        abort(400)

    user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json.get("name", ""),
        'password': request.json['password'],
        'id': random.randint(1,1000)
    }
    return jsonify({'status': add_user(user)}), 201

@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def add_user(new_user):
    user_list = []
    print(new_user)

    db = connection.cloud_native.users
    user = db.find({"$or": [{"username": new_user["username"]}, {"email": new_user["email"]} ]})
    for i in user:
        print(str(i))
        user_list.append(i)
    if user_list == []:
        db.insert_one(new_user)
        return "Sucess!"
    else:
        abort(409)

# DELETE user information
@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(404)
    user = request.json['username']
    return jsonify({'status': del_user(user)}), 200

def del_user(del_user):
    db = connection.cloud_native.users
    user_list = []
    for i in db.find({'username': del_user}):
        user_list.append(i)
    if user_list == []:
        abort(404)
    else:
        db.remove({'username': del_user})
        return "Sucess"

# PUT, update user information
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = {}
    if not request.json:
        abort(400)
    user['id'] = user_id
    key_list = request.json.keys()
    for i in key_list:
        user[i] = request.json[i]
    print(user)
    return jsonify({'status': upd_user(user)}), 200

def upd_user(user):
    user_list = []
    print(user)
    db_user = connection.cloud_native.users
    users = db_user.find_one({"id": user['id']})
    for i in users:
        user_list.append(str(i))
    if user_list == []:
        abort(409)
    else:
        db_user.update({"id": user["id"]}, {'$set': user})
        return "Sucess!"

# ------------------------------------------------------------------------------------------------------------
# api v2
@app.route('/api/v2/tweets', methods=['GET'])
def get_tweets():
    return list_tweets()

def list_tweets():
    tweet_list = []
    db = connection.cloud_native.tweets
    for row in db.find():
        tweet_list.append(str(row))

    return jsonify({'tweets_list': tweet_list})

@app.route('/api/v2/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    return list_tweet(id)

def list_tweet(user_id):
    db = connection.cloud_native.tweets
    tweet_list = []
    tweet = db.find({'id': user_id})
    for i in tweet:
        tweet_list.append(str(i))
    if tweet_list == []:
        abort(404)
    return jsonify({'tweet': tweet_list})

@app.route('/api/v2/tweets', methods=['POST'])
def add_tweets():
    user_tweet = {}
    if not request.json or not 'username' in request.json or not 'body' in request.json:
        abort(400)

    user_tweet['username'] = request.json['username']
    user_tweet['body'] = request.json['body']
    user_tweet['tweetedby'] = request.json['username']
    user_tweet['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    print(user_tweet)

    return jsonify({'status': add_tweet(user_tweet)}), 201


# add tweet for someone
def add_tweet(new_tweets):
    tweet_list = []
    print(new_tweets)
    db_user = connection.cloud_native.users
    db_tweet = connection.cloud_native.tweets
    user = db_user.find({"username": new_tweets['tweetedby']})
    for i in user:
        tweet_list.append(str(i))
    if tweet_list == []:
        abort(404)
    else:
        db_tweet.insert(new_tweets)
        return "Sucess!"

# -----------------------------------------------------------------------------------------------------
# frontend logic
@app.route('/adduser')
def adduser():
    return render_template('addusers.html')

@app.route('/addtweets')
def addtweets():
    return render_template('addtweets.html')

# ----------------------------------------------------------------------------------------
# security
def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def main():
    sumSessionCounter()
    return render_template('main.html')

@app.route('/addname')
def addname():
    sumSessionCounter()
    if request.args.get('yourname'):
        session['name'] = request.args.get('yourname')
        return redirect(url_for('main'))
    else:
        return render_template('addname.html', session=session)

@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('main'))

if __name__ == '__main__':
    create_mongodatabase()
    app.run('127.0.0.1', port=5000, debug=True)