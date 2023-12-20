from app import app
from flask import request
from app.controller import DosenController, UserController, AuthController

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/dosen', methods=['GET', 'POST'])
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.store()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenShow(id):
    if request.method == 'PUT':
        return DosenController.update(id)
    elif request.method == 'GET':
        return DosenController.show(id)
    else:
        return DosenController.delete(id)

@app.route('/users', methods=['POST'])
def users():
    return UserController.store()

@app.route('/auth/login', methods=['POST'])
def login():
    return AuthController.login()