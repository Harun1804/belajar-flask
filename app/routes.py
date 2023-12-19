from app import app
from flask import request
from app.controller import DosenController

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/dosen', methods=['GET', 'POST'])
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    else:
        return DosenController.store()

@app.route('/dosen/<id>', methods=['GET'])
def dosenShow(id):
    return DosenController.show(id)