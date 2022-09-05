import os
import psycopg2
import json

os.system("createdb webserver")

config_file = open("config.json")

json = json.load(config_file)

conn = psycopg2.connect(
    user=json["user"],
    password=json["password"],
    host=json["host"],
    port=json["port"],
    dbname=json["dbname"],
)

conn.autocommit = True
cursor = conn.cursor()

create_table = """CREATE TABLE PEOPLE(
    ID INT PRIMARY KEY NOT NULL,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    DOB DATE
    )"""

cursor.execute(create_table)
conn.close()
