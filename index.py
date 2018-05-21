from flask import Flask
import util.db as db

from router.home import home
from router.file import file_api

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(file_api)

db.init()

if __name__ == '__main__':
  # app.debug = True
  app.run(host='0.0.0.0', port=80)
  app.run()