import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='ren',
        password='iot159487',
        db='juego'
    )
    if connection.is_connected():
        print("Connected.")
except Exception as ex:
    print(Ex)
