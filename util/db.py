import sqlite3
import datetime

def init():
  conn = sqlite3.connect('file.db')
  cur = conn.cursor()

  # cur.execute('DROP TABLE IF EXISTS attachments')

  sql = '''CREATE TABLE IF NOT EXISTS attachments(id TEXT PRIMARY KEY, fileName TEXT, realPath TEXT, mime TEXT, fileSize INTEGER, create_at TEXT)'''
  cur.execute(sql)

  conn.commit()
  conn.close()

def insert(tup):
  conn = sqlite3.connect('file.db')
  cur = conn.cursor()

  sql = 'INSERT INTO attachments(id, fileName, realPath, mime, fileSize, create_at) values (?, ?, ?, ?, ?, ?)'
  data = (tup['id'], tup['fileName'], tup['realPath'], tup['mime'], tup['fileSize'], datetime.datetime.now())

  cur.execute(sql, data)
  
  conn.commit()
  conn.close()
  print('insert sueccess : ' + tup['id'])

def select(key):
  conn = sqlite3.connect('file.db')
  cur = conn.cursor()
  
  sql = 'SELECT * FROM attachments WHERE id=?'
  cur.execute(sql, (key,))
  
  result = cur.fetchall()
  conn.close()
  return result

def all():
  conn = sqlite3.connect('file.db')
  cur = conn.cursor()
  
  sql = 'SELECT * FROM attachments'
  cur.execute(sql)
  
  result = cur.fetchall()
  conn.close()
  return result
