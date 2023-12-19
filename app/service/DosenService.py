from app import db
from app.model.dosen import Dosen
from app.service.MahasiswaService import findByDosen

def index():
  dosen = Dosen.query.all()
  data = formatArray(dosen)
  return data

def find(id):
  dosen = Dosen.query.filter_by(id = id).first()
  mahasiswa = findByDosen(id)
  data = singleTransformWithMahasiswa(dosen, mahasiswa)
  return data

def store(nidn, name, phone, address):
  dosen = Dosen(nidn=nidn, name=name, phone=phone, address=address)
  db.session.add(dosen)
  db.session.commit()

def update(id, nidn, name, phone, address):
  dosen = Dosen.query.filter_by(id = id).first()
  dosen.nidn = nidn
  dosen.name = name
  dosen.phone = phone
  dosen.address = address
  db.session.commit()

def delete(id):
  dosen = Dosen.query.filter_by(id = id).first()
  if not dosen:
    return False

  db.session.delete(dosen)
  db.session.commit()

def formatArray(lists):
  array = []
  for list in lists:
    array.append(singleTransform(list))
  
  return array

def singleTransform(data):
  data = {
    'id': data.id,
    'nidn': data.nidn,
    'name': data.name,
    'phone': data.phone,
    'address': data.address
  }

  return data

def singleTransformWithMahasiswa(data, mahasiswa):
  data = {
    'id': data.id,
    'nidn': data.nidn,
    'name': data.name,
    'phone': data.phone,
    'address': data.address,
    'mahasiswa': mahasiswa
  }

  return data