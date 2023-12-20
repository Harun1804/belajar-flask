from app import db
from app.model.user import User

def store(name, email, password, level = 1):
  user = User(name=name, email=email, level=level)
  user.setPassword(password)
  db.session.add(user)
  db.session.commit()