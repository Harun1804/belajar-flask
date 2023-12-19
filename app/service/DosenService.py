from app import db
from app.model.dosen import Dosen
from app.service.MahasiswaService import findByDosen

def index():
  try:
    dosen = Dosen.query.all()
    data = formatArray(dosen)
    return data
  except Exception as e:
    print(e)

def find(id):
  try:
    dosen = Dosen.query.filter_by(id = id).first()
    mahasiswa = findByDosen(id)
    data = singleTransformWithMahasiswa(dosen, mahasiswa)
    return data
  except Exception as e:
    print(e)

def store(nidn, name, phone, address):
  dosen = Dosen(nidn=nidn, name=name, phone=phone, address=address)
  db.session.add(dosen)
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