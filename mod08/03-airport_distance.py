import mysql.connector
from geopy.distance import great_circle


def calculate_distance(icao1, icao2, cursor):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident in ('{icao1}','{icao2}')"
#    print(sql)
    cursor.execute(sql)
    orig = None
    orig_name = None
    dest = None
    dest_name = None
#    print(cursor)
    for name, latitude_deg, longitude_deg in cursor:
        if orig is None:
            orig = (latitude_deg, longitude_deg)
            orig_name = name
        else:
            dest = (latitude_deg, longitude_deg)
            dest_name = name
    distance = great_circle(orig, dest).km
    return orig_name, dest_name, distance


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='python',
    password='python',
    autocommit=True
)
cursor = connection.cursor()

icao1 = input("Input ICAO of origin airport: ")
icao2 = input("Input ICAO of destination airport: ")
orig_name, dest_name, distance = calculate_distance(icao1, icao2, cursor)
print(f"Distance between {orig_name} {icao1} and {dest_name} {icao2} is {distance:.2f} km.")