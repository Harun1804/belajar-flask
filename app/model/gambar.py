from app import db
from datetime import datetime

class Gambar(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50), nullable=False)
  pathname = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self): # string representation of the model
    return '<Gambar {}>'.format(self.name)