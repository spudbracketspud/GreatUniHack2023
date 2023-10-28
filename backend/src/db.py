import mysql.connector as mc

def createDB():
    try:
        conn = mc.connect(host='localhost', user='root', password='rootroot')
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS logAlog")
        conn.commit()
        conn.close()
    except mc.Error as e:
        print(f"Error creating database: {e}")

def createTable():
    try:
        conn = mc.connect(host='localhost', user='root', password='rootroot', database='logAlog')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS amazonImg (idpic INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, capture LONGBLOB NOT NULL)")
        conn.commit()
        conn.close()
    except mc.Error as e:
        print(f"Error creating table: {e}")

def insertData():
    try:
        conn = mc.connect(host='localhost', user='root', password='rootroot', database='logAlog')
        cur = conn.cursor()
        insertQuery = "INSERT INTO amazonImg (capture) VALUES (%s)"
        data = (convertToBinaryData("greenCubeTest.jpeg"),)
        cur.execute(insertQuery, data)
        conn.commit()
        conn.close()
    except mc.Error as e:
        print(f"Error inserting data: {e}")

# Call the functions
createDB()
createTable()
insertData()

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
  
