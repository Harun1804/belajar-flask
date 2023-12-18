from app import db
from datetime import datetime

class Dosen(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  nidn = db.Column(db.String(30), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  phone = db.Column(db.String(15))
  address = db.Column(db.String(250))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self): # string representation of the model
    return '<Dosen {}>'.format(self.name)