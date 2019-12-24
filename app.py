# -*- utf-8 -*-
import json
import sqlite3

from flask import Flask, jsonify, make_response, request, abort

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

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)