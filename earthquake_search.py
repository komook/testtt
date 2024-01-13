import requests
import sqlite3
# get_starttime = (input('starttime: '))
# get_endtime = (input('endtime: '))
# get_latitude = (input('latitude: '))
# get_longitude = (input('longitude: '))
# get_maxradiuskm = (input('maxradiuskm: '))
# get_minmagnitude = (input('minmagnitude: '))

    # 'format':'geojson',
    # 'starttime':'2019-01-01',
    # 'endtime':'2019-02-01',
    # 'latitude':'51.51',
    # 'longitude':'-0.12',
    # 'maxradiuskm':'2000',
    # 'minmagnitude':'2',

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

response = requests.get(url, headers={'Accept':'application/json'}, params={
    'format':'geojson',                             
    'starttime':'2019-01-01',
    'endtime':'2019-02-01',
    'latitude':'51.51',
    'longitude':'-0.12',
    'maxradiuskm':'2000',
    'minmagnitude':'2',
    
})
data = response.json()
get_len = len(data['features'])
i = 0

u = []

while i <= get_len - 1:
    result_place = data['features'][i]['properties']['place']
    result_mag = data['features'][i]['properties']['mag']
    u.append((result_place, str(result_mag)))
    # print('earthquake number - {} | place: {} | magnitude: {}'.format(i, result_place, result_mag ))
    i += 1

print(u)
conn = sqlite3.connect("earthquake.db")

cursor = conn.cursor()

# earthquake_table = "CREATE TABLE earthquake (place_char TEXT, mag_char TEXT)"

# insert_query = "INSERT INTO earthquake VALUES (?, ?);"

# cursor.executemany(insert_query, u)



conn.commit()

conn.close()