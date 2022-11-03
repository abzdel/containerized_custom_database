import sqlite3

connection = sqlite3.connect("mydb.db")
cursor = connection.cursor()

table = """create table if not exists college_admissions(
        serial_no int PRIMARY_KEY,
        gre int,
        toefl int,
        university_rating int,
        sop float,
        lor float,
        cgpa float,
        research int,
        chance_of_admit float
    )"""


cursor.execute(table)

cursor.execute("insert into table values ()")