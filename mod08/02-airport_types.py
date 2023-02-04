import mysql.connector


def search(cc):
    sql = "SELECT type, COUNT(*) FROM airport"
    sql += " WHERE iso_country='" + cc + "' GROUP BY type"
#    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for result in result:
            print(f"There are {result[1]} {result[0]} in {cc} ")


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='python',
    password='python',
    autocommit=True
)

cc = input("Input two letter country code: ").upper()
search(cc)
