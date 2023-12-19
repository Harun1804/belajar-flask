from app import response
from flask import request
from app.service import DosenService

def index():
  try:
    data = DosenService.index()
    return response.success(data, "success")
  except Exception as e:
    print(e)

def show(id):
  try:
    data = DosenService.find(id)
    if not data:
      return response.badRequest([], 'Data not found')
    return response.success(data, "success")
  except Exception as e:
    print(e)