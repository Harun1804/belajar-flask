import os
import uuid
from app.model.gambar import Gambar
from app import db
from app.config import media
from werkzeug.utils import secure_filename

def upload(judul, files):
  if 'file' not in files:
    return {
      'message': 'File tidak ditemukan',
      'status': False,
    }

  file = files['file']
  if file.filename == '':
    return {
      'message': 'File tidak tersedia',
      'status': False,
    }

  if file and media.allowed_file(file.filename):
    uid = uuid.uuid4()
    filename = secure_filename(file.filename)
    renamefile = 'flask-'+str(uid)+'-'+filename

    file.save(os.path.join(media.UPLOAD_FOLDER, renamefile))

    upload = Gambar(name=judul, pathname=renamefile)
    db.session.add(upload)
    db.session.commit()
    return {
      'data' : {
        'id': upload.id,
        'name': upload.name,
        'pathname': upload.pathname,
      },
      'message': 'File berhasil diupload',
      'status': True,
    }
