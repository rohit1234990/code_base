from flask import Blueprint, request, jsonify
from db_helper import connect, insert, select_one, select_all, delete_helper
import jwt, hashlib, os


user = Blueprint('user', __name__)

def md5_hash(password):
    hash = hashlib.md5()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()


# create user routes here
@user.route('/register', methods = ['POST'])
def create():
    name = request.json['name']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    
    query = "INSERT INTO `users` (`name`, `email`, `username`, `password`,`joined_on`) VALUES (%s, %s, %s, %s, CURDATE())"
    arguments = [name, email, username, md5_hash(password)]
    
    return jsonify(insert(query, arguments))

@user.route('/edit/<int:user_id>', methods = ['PUT'])
def edit(user_id):
    name     = request.json['name']
    email    = request.json['email']
    username = request.json['username']
    password = request.json['password']

    user = {'name': name, 'email': email, 'username': username, 'password': password}
    return jsonify(user)

@user.route('/delete/<int:user_id>', methods = ['DELETE'])
def delete():
    pass

@user.route('/login', methods = ['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    # get the token back
    query = "SELECT user_id, name FROM `user` WHERE `username` = %s AND `password` = %s"
    arguments = [username, md5_hash(password)]
    result = select_one(query, arguments)
    if result['result'] == 'success':
        token = jwt.encode(result['data'], 'secret', algorithm='HS256')
        data = {'token': token, 'user_id': result['data']['user_id']}
        return jsonify({'result':'success', 'data': data})
    else:
        return jsonify({'result':'failure'})




