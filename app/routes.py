from app import app
from app.controller import DosenController

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/dosen', methods=['GET'])
def dosen():
    return DosenController.index()

@app.route('/dosen/<id>', methods=['GET'])
def dosenShow(id):
    return DosenController.show(id)