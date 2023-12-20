from app.util import response
from flask import request
from app.service import AuthService
from app.schema.LoginSchema import LoginSchema

def login():
  try:
    errors = LoginSchema().validate(request.form)
    if errors:
      return response.validateError([], errors)

    data = AuthService.login(request.form)
    if not data['status']:
      return response.badRequest([], data['message'])
    return response.success(data, "Successfully login")
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }