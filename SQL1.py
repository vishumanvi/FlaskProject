import sqlite3

conn = sqlite3.connect("testdatabase.db")

cur = conn.cursor()

# cur.execute("create table population (city text, state text, population int)")

populations = [('Belgaum', 'Karnataka', 500000),('Mangalore','Karnataka',400000)]

cur.executemany('insert into population values (?,?,?)', populations)

conn.commit()
