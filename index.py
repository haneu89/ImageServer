import os
from flask import Flask, render_template, request, redirect, url_for, send_file
import datetime
import uuid
import time
import random
from util.base62 import encode
import util.db as db

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

allowed_file = lambda filename : '.' in filename and filename.split('.').pop() in ALLOWED_EXTENSIONS
randFileName = lambda filename : '{}.{}'.format(str(uuid.uuid4()), filename.split('.').pop())
curNum = lambda: int(round(time.time()) % 100000000)
ranNum = lambda: random.randrange(100, 999)

app = Flask(__name__)

db.init()

def savePath():
  UPLOAD_FOLDER = 'upload/' + datetime.datetime.today().strftime('%Y/%m/%d')
  os.makedirs(UPLOAD_FOLDER, exist_ok=True)
  return UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def main():
  # print(db.all())
  return render_template('home.html')

@app.route('/<id>', methods=['GET'])
def fileDown(id) :
  if not db.select(id):
    return 'no'
  else :
    result = db.select(id)[0]
    return send_file(result[2], mimetype=result[3],as_attachment=True, attachment_filename=result[1])

@app.route('/', methods=['POST'])
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


if __name__ == '__main__':
  # app.debug = True
  app.run(host='0.0.0.0', port=80)
  app.run()