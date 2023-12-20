import os

basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])

UPLOAD_FOLDER=os.environ.get('UPLOAD_FOLDER')
MAX_CONTENT_LENGTH = 2 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS