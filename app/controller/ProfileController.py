from app.util import response
from flask import request
from app.service import AuthService

def userLogin():
  try:
    data = AuthService.userLogin()
    return response.success(data, "Get User Login Profile")
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }