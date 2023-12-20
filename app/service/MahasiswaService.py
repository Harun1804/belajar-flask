from app.model.mahasiswa import Mahasiswa

def index():
  try:
    mahasiswa = Mahasiswa.query.all()
    data = formatArray(mahasiswa)
    return data
  except Exception as e:
        return {
      'message': str(e),
      'status': False,
    }

def findByDosen(dosen_id):
  try:
    mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == dosen_id) | (Mahasiswa.dosen_dua == dosen_id))
    data = formatArray(mahasiswa)
    return data
  except Exception as e:
        return {
      'message': str(e),
      'status': False,
    }

def formatArray(lists):
  array = []
  for list in lists:
    array.append(singleTransform(list))
  
  return array

def singleTransform(data):
  data = {
    'id': data.id,
    'nim': data.nim,
    'name': data.name,
    'phone': data.phone,
    'address': data.address,
    'major' : data.major,
    'dosen_satu' : data.dosen_satu,
    'dosen_dua' : data.dosen_dua,
  }

  return data