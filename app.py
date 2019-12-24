# -*- utf-8 -*-
import json
import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Nothing'

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

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()

def list_users():
    conn = sqlite3.connect('app.db')
    print('Open Database Sucessful!')
    api_list = []
    cursor = conn.execute('select username, full_name, emailid, password, id from users')
    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['full_name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'user_list':api_list})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)