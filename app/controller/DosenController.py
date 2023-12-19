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

def store():
  try:
    nidn = request.form.get('nidn')
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    DosenService.store(nidn, name, phone, address)
    return response.success([], "Dosen has been created")
  except Exception as e:
    print(e)

def update(id):
  try:
    nidn = request.form.get('nidn')
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    DosenService.update(id, nidn, name, phone, address)
    return response.success([], "Dosen has been updated")
  except Exception as e:
    print(e)

def delete(id):
  try:
    DosenService.delete(id)
    return response.success([], "Dosen has been deleted")
  except Exception as e:
    print(e)