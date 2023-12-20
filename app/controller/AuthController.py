from app.util import response
from flask import request
from app.service import AuthService

def login():
  try:
    email = request.form.get('email')
    password = request.form.get('password')
    data = AuthService.login(email, password)
    if not data['status']:
      return response.badRequest([], data['message'])
    return response.success(data, "Successfully login")
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }

def userLogin():
  try:
    data = AuthService.userLogin()
    return response.success(data, "Get User Login Profile")
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }