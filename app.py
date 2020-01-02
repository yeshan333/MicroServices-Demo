# -*- utf-8 -*-

import json
import sqlite3

from flask import Flask, jsonify, make_response, request, abort
from time import strftime, gmtime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Nothing'

# get api information
@app.route('/api/v1/info')
def home_index():
    conn = sqlite3.connect('app.db')
    print('Open Database Sucessful !')

    api_list = []
    cursor = conn.execute('SELECT buildtime, version, methods, links from apirelease')

    for row in cursor:
        api = {}
        api['version'] = row[0]
        api['buildtime'] = row[1]
        api['methods'] = row[2]
        api['links'] = row[3]
        api_list.append(api)
    conn.close()
    return jsonify({'api_version': api_list}), 200

# get user information
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    return list_users(user_id)

def list_users(user_id):
    conn = sqlite3.connect('app.db')
    print('Open Database Sucessful!')
    api_list = []
    # cursor = conn.execute('select username, full_name, emailid, password, id from users')
    cursor = conn.execute('select * from users where id=?',(user_id, ))
    data = cursor.fetchall()
    if len(data) != 0:
        user = {}
        user['username'] = data[0][0]
        user['email'] = data[0][1]
        user['password'] = data[0][2]
        user['full_name'] = data[0][3]
        user['id'] = data[0][4]
        api_list.append(user)
    conn.close()
    return jsonify({'user_list':api_list})

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
        'full_name': request.json['username'],
        'password': request.json['password'],
        'id': request.json['id']
    }
    return jsonify({'status': add_user(user)}), 201

@app.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def add_user(new_user):
    conn = sqlite3.connect('app.db')
    print('Open Database Sucessful!')
    api_list = []
    cursor = conn.cursor()
    cursor.execute('select * from users where username=? or emailid=?', \
        (new_user['username'], new_user['email']))
    data = cursor.fetchall()
    if len(data) != 0:
        abort(409)
    else:
        cursor.execute('insert into users values(?,?,?,?,?)', (new_user['username'], \
            new_user['email'], new_user['password'], new_user['full_name'], new_user['id']))
        # assert 1==2
        conn.commit()
        conn.close()
        return "Sucess!"
    conn.close()
    return "Failed !"

# DELETE user information
@app.route('/api/v1/users', methods=['DELETE'])
def delete_user():
    if not request.json or not 'username' in request.json:
        abort(404)
    user = request.json['username']
    return jsonify({'status': del_user(user)}), 200

def del_user(del_user):
    conn = sqlite3.connect('app.db')
    print('Open Database Sucessfule!')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where username=?", (del_user,))
    data = cursor.fetchall()
    print('Data: ', data)
    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("DELETE FROM users WHERE username=?", (del_user,))
        conn.commit()
        conn.close()
        return "Sucess"
    conn.close()
    return "Failed"

# PUT,update user information
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
    conn = sqlite3.connect('app.db')
    print("Opend database sucessfully!")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user['id'],))
    data = cursor.fetchall()
    if data == 0:
        abort(404)
    else:
        key_list = user.keys()
        for i in key_list:
            if i != "id":
                print(user, i)
                cursor.execute("UPDATE users SET {0}=? WHERE id=?".format(i), (user[i], user["id"]))
                conn.commit()
                conn.close()
        return "Sucess"
    return "Failed"

# ------------------------------------------------------------------------------------------------------------

@app.route('/api/v2/tweets', methods=['GET'])
def get_tweets():
    return list_tweets()

def list_tweets():
    conn = sqlite3.connect('app.db')
    print("Open Database Sucessful!")
    api_list = []
    cursor = conn.execute('SELECT username, body, tweet_time, id FROM tweets')
    data = cursor.fetchall()
    print(data)
    if data!=0:
        for row in data:
            tweets = {}
            tweets['Tweet By'] = row[0]
            tweets['Body'] = row[1]
            tweets['TimeStamp'] = row[2]
            tweets['id'] = row[3]
            api_list.append(tweets)
    else:
        return api_list
    conn.close()
    return jsonify({'tweets_list': api_list})

@app.route('/api/v2/tweets/<int:id>', methods=['GET'])
def get_tweet(id):
    return list_tweet(id)

def list_tweet(user_id):
    conn = sqlite3.connect('app.db')
    print("OPen Database Sucessful!")
    # api_list = []
    cursor = conn.execute("SELECT id, username, body, tweet_time FROM tweets WHERE id=?", (user_id, ))
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        abort(404)
    else:
        user = {}
        user['id'] = data[0][0]
        user['username'] = data[0][1]
        user['body'] = data[0][2]
        user['tweet_time'] = data[0][3]
    conn.close()
    return jsonify(user)

@app.route('/api/v2/tweets', methods=['POST'])
def add_tweets():
    user_tweet = {}
    if not request.json or not 'username' in request.json or not 'body' in request.json:
        abort(400)

    user_tweet['username'] = request.json['username']
    user_tweet['body'] = request.json['body']
    user_tweet['created_at'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    print(user_tweet)

    return jsonify({'status': add_tweet(user_tweet)}), 201


# add tweet for someone
def add_tweet(new_tweets):
    conn = sqlite3.connect('app.db')
    print('Open Dataabase Sucessful!')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (new_tweets['username'],))
    data = cursor.fetchall()

    if len(data) == 0:
        abort(404)
    else:
        cursor.execute("INSERT INTO tweets (username, body, tweet_time) VALUES(?,?,?)", (new_tweets['username'], \
            new_tweets['body'], new_tweets['created_at']))
        conn.commit()
        conn.close()
        return "Sucess"
    return "Failed"

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)