"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
from utils import *
from classes import Table
import psycopg2

employees_data = read_csv('north_data/employees_data.csv')
employees_table = Table(employees_data)
print(get_sql_command(employees_table))

#Подключаемся к БД
conn = psycopg2.connect(host="localhost",
                        database="north",
                        user="postgres",
                        password="Subbotin1")
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute(get_sql_command(employees_table))
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()