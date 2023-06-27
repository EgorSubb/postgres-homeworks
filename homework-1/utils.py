import csv
from classes import Table


def read_csv(path_to_csv):
    with open(path_to_csv, newline='', encoding='utf-8') as f:
        data = list(csv.reader(f, quotechar='"'))
        columns_name = data[0]
        data_for_columns = []
        for row in data[1::]:
            data_for_columns.append(tuple(row))
        table_name = path_to_csv.split("/")[1].split("_")[0]

        return tuple(columns_name), data_for_columns, table_name


def get_sql_command(object_table: Table):
    return f"INSERT INTO {object_table.name} VALUES {object_table.columns}, {tuple(object_table.data)}"


print(read_csv('north_data/employees_data.csv'))
# print(get_sql_command(read_csv('north_data/employees_data.csv')))


