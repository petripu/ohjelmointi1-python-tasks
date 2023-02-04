import mysql.connector


def search(icao):
    sql = "SELECT Ident, Name, Municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for line in result:
            print(f"ICAO code {line[0]} found airport {line[1]} located in {line[2]} ")


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='python',
    password='python',
    autocommit=True
)

icao = input("Input ICAO code: ").upper()
search(icao)
