import sys
import sqlite3

file = sys.argv[1]
db = sys.argv[2]

conn = sqlite3.connect(db)
c = conn.cursor()
import csv
c.execute("delete from route")
with open(file, newline='',encoding="utf8") as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        sql = "INSERT INTO route VALUES ('" + row["route_type"] + "','" + row["route_id"] + "','"
        sql = sql + row["route_short_name"] + "','"
        sql = sql + row["route_long_name"].replace("'","") + "','"
        sql = sql + row["agency_id"] + "','"
        sql = sql + row["route_desc"].replace("'","") + "','"
        sql = sql + row["route_url"] + "','"
        sql = sql + row["route_color"] + "','"
        sql = sql + row["route_text_color"] + "')"
        c.execute(sql)
conn.commit()
conn.close()