import pyodbc
import pandas as pd
import server_info


def create_conection():
    # # para linux, escolher uma das duas opções:
    # driver = 'ODBC Driver 17 for SQL Server'
    # drivers = [item for item in pyodbc.drivers()]
    # driver = drivers[-1]

    # # para windows
    driver = 'SQL Server'

    # # dados servidor
    server = server_info.server
    database = server_info.database
    uid = server_info.uid
    pwd = server_info.pwd
    con_string = f'DRIVER={driver};SERVER={server};UID={uid};PWD={pwd};DATABASE={database}'
    # print(con_string)
    cnxn = pyodbc.connect(con_string)

    return cnxn


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f'Error {err}')


def columns_names(connection, tabel, create_file=False):

    query = f"""
        SELECT OBJECT_SCHEMA_NAME (c.object_id) SchemaName,
                o.Name AS Table_Name, 
                c.Name AS Field_Name,
                t.Name AS Data_Type,
                t.max_length AS Length_Size,
                t.precision AS Precision
        FROM sys.columns c 
             INNER JOIN sys.objects o ON o.object_id = c.object_id
             LEFT JOIN  sys.types t on t.user_type_id  = c.user_type_id   
        WHERE o.type = 'U'
        and o.Name = '{tabel}'
        ORDER BY o.Name, c.Name"""
    results = read_query(connection, query)
    colunas = str()
    for result in results:
        print(result[2])
        colunas += '\n' + result[2]

    if create_file:
        with open('colunas.txt', 'w') as f:
            f.write(colunas)


def print_dataframe(connection, dataframe):
    cursor = connection.cursor()
    cursor.execute(f"select * from [{dataframe}]")
    for row in cursor:
        print(row)


if __name__ == '__main__':
    connection = create_conection()
    # columns_names(connection, tabel="CT2010", create_file=True)
    # print_dataframe(connection, dataframe="CT2010")

