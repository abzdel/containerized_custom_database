import sqlite3
import pandas as pd


# read in admissions data to dataframe
df = pd.read_csv("adm_data.csv", names = ["serial_no", "gre", "toefl", "university_rating", "sop", "lor", "cgpa", "research", "chance_of_admit"], header=0)


# drop college_admissions table if it exists
# not currently using - uncomment to debug table creation step
# cursor.execute("drop table if exists college_admissions")



# create local sql database
connection = sqlite3.connect("mydb.db")

# define query to create table
create_sql = "create table if not exists college_admissions (serial_no int PRIMARY_KEY, gre int, toefl int, university_rating int, sop float, lor float, cgpa float, research int, chance_of_admit float);"
cursor = connection.cursor()
cursor.execute(create_sql)


# send our df data to our table
df.to_sql("college_admissions", connection, if_exists="replace", index=False)


# test query to make sure it works
print(cursor.execute("select serial_no from college_admissions limit 5").fetchall())