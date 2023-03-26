import psycopg2
import csv

conn = psycopg2.connect(
    database="company_development",
    user="postgres"
)

with open('company-data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

cursor = conn.cursor()
breakpoint()

sql_insert = "INSERT INTO companies (index, id, name, website, country, description, founded, industry, employees) VALUES (%s,%s, %s, %s,%s, %s, %s,%s, %s)"
values = [tuple(row) for row in data]
breakpoint()
for value in values[1:-1]:
    cursor.execute(sql_insert, value)

conn.commit()
