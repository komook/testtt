import sqlite3



conn = sqlite3.connect("earthquake.db")


cursor = conn.cursor()

# earthquake_table = "CREATE TABLE earthquake (place_char TEXT, mag_char TEXT)"

# insert_query = "INSERT INTO earthquake VALUES (?, ?);"

# cursor.executemany(insert_query, u)



conn.commit()

conn.close()