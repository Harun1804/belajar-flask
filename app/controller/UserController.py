from app import response
from flask import request
from app.service import UserService

def store():
  try:
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    level = request.form.get('level')
    UserService.store(name, email, password, level)
    return response.success([], "User has been created")
  except Exception as e:
    print(e)