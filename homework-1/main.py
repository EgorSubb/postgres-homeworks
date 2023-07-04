"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
from utils import *
from classes import Table
import psycopg2

# employees_data = read_csv('north_data/employees_data.csv')
# employees_table = Table(employees_data)
# print(get_sql_command(employees_table))
#
# #Подключаемся к БД
# conn = psycopg2.connect(host="localhost",
#                         database="north",
#                         user="postgres",
#                         password="Subbotin1")
# try:
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(get_sql_command(employees_table))
#             rows = cur.fetchall()
#             for row in rows:
#                 print(row)
# finally:
#     conn.close()

# Подключаемся к БД
conn = psycopg2.connect(host="localhost",
                        database="north",
                        user="postgres",
                        password="Subbotin1")

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/customers_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        row
                    )

finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/employees_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                        row
                    )
finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                        row
                    )
finally:
    conn.close()
