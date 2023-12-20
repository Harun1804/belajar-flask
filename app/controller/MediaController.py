from app.util import response
from flask import request
from app.service import GambarService

def store():
  try:
    data = GambarService.upload(request.form.get('judul'), request.files)
    if not data['status']:
      return response.badRequest([], data['message'])
    return response.success(data['data'], data['message'])
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }