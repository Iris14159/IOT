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
        info_server = connection.get_server_info()
        print(info_server)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Data base: {}".format(row))
except Exception as ex:
    print(Ex)
finally:
    if connection.is_connected():
        connection.close()
        print("Connection finished.")
