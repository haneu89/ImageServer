from flask import Blueprint, send_file, request
import util.db as db
import os
import uuid
import time
import random
from util.base62 import encode
import datetime

file_api = Blueprint('file', __name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

allowed_file = lambda filename : '.' in filename and filename.split('.').pop() in ALLOWED_EXTENSIONS
randFileName = lambda filename : '{}.{}'.format(str(uuid.uuid4()), filename.split('.').pop())
curNum = lambda: int(round(time.time()) % 100000000)
ranNum = lambda: random.randrange(100, 999)

def savePath():
  UPLOAD_FOLDER = 'upload/' + datetime.datetime.today().strftime('%Y/%m/%d')
  os.makedirs(UPLOAD_FOLDER, exist_ok=True)
  return UPLOAD_FOLDER

@file_api.route('/<id>', methods=['GET'])
def fileDown(id) :
  if not db.select(id):
    return 'no'
  else :
    result = db.select(id)[0]
    return send_file(result[2], mimetype=result[3],as_attachment=True, attachment_filename=result[1])

@file_api.route('/', methods=['POST'])
def upload():
  file = request.files['file']
  if file and allowed_file(file.filename):
    filename = randFileName(file.filename)
    fullPath = os.path.join(savePath(), filename)

    file.save(fullPath)

    key = ''
    while True:
      key = encode(int("{}{}".format(curNum(), ranNum())))
      if not db.select(key):
        break

    db.insert({
      'id'      : key,
      'fileName': file.filename,
      'realPath': fullPath,
      'mime'    : file.content_type,
      'fileSize': os.stat(fullPath).st_size
    })
    
    return key
