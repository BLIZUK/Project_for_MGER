import sqlite3 as sq

with sq.connect("ACTIVlist.db") as con:
    cur = con.cursor()

