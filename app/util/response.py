from flask import jsonify, make_response

def success(values = [], message = 'success', code = 200):
  response = {
      'message': message,
      'data': values
  }
  return make_response(jsonify(response)), code

def badRequest(values = [], message = 'bad request', code = 400):
  response = {
    'message': message,
    'data' : values
  }

  return make_response(jsonify(response)), code

def validateError(values = [], message = 'validate error', code = 422):
  response = {
    'message': message,
    'data': values
  }

  return make_response(jsonify(response)), code