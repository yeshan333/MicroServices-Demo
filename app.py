# -*- utf-8 -*-
import json
import sqlite3

from flask import Flask, jsonify, make_response

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

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)