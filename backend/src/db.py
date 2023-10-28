import bcrypt as bc
import mysql.connector as sr

def createDBs():
  
  try:
      conn = sr.connect(host='localhost', user='root', database='logAlog')
  except:
      try:
          conn = sr.connect(host='localhost', user='root',
                            password="root", database='logAlog')
      except:
          conn = sr.connect(host='localhost', user='root',
                            database='logAlog', password='rootroot')
  cur = conn.cursor()
  cur.execute("CREATE database IF NOT EXISTS logAlog")
  cur.execute("USE logAlog")
  
