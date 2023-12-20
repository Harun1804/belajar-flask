from app import db
from app.model.user import User
from app.service.UserService import singleTransform
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
import datetime

def login(email, password):
  try:
    user = User.query.filter_by(email=email).first()

    if not user:
      return {
        'message': 'User not found',
        'status': False
      }

    if not user.checkPassword(password):
      return {
        'message': 'Password is wrong',
        'status': False
      }

    data = singleTransform(user)
    expires = datetime.timedelta(days=7)
    expiores_refresh = datetime.timedelta(days=7)
    access_token = create_access_token(data, expires_delta=expires)
    refresh_token = create_refresh_token(data, expires_delta=expiores_refresh)

    return {
      'status' :True,
      'access_token': access_token,
      'refresh_token': refresh_token,
      'user': data
    }
  except Exception as e:
    return {
      'message': str(e),
      'status': False,
    }

def userLogin():
  return get_jwt_identity()