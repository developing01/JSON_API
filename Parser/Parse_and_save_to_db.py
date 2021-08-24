import requests
from time import time
import psycopg2


def parser_csv(company, start_date):
    '''Метод для ортимання запиту'''

    my_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                               ' Chrome/86.0.4240.185 YaBrowser/20.11.2.78 Yowser/2.5 Safari/537.36', 'accept': '*/*'}

    current_time = int(time())
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{company}?period1={start_date}&period2={current_time}&interval=1d&events=history&includeAdjustedClose=true'
    print('Request created')
    return requests.get(url, headers=my_header)


def save_data_to_csv_file(file_name, request):
    '''Метод для запису отриманих даних в csv файл'''

    with open(f'/home/user/PycharmProjects/Pars_project/csv_data/{file_name}', 'w') as output_file:
        output_file.write(request.text)
    print('File recorded')


def connection_to_bd():
    '''Метод для підключення до БД'''
    con = psycopg2.connect(
        database="Company_data",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    print('Connection to postgres')
    return con


def create_table_to_bd(company_name, connect):
    '''Метод для створення таблиці з назвою компанії'''
    cursor = connect.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {company_name}   
         (DATE CHAR(10),
         OPEN FLOAT,
         HIGH FLOAT,
         LOW FLOAT,
         CLOSE FLOAT,
         ADJ_CLOSE FLOAT,
         volume INT);''')
    print("Table created successfully")
    connect.commit()
    connect.close()
    print('Connection closed')


def saved_data_to_table(table_name, connect):
    '''Метод для запису csv файла в БД'''
    cursor = connect.cursor()
    table_name_lower = table_name.lower()
    open_file = open(f'/home/user/PycharmProjects/Pars_project/csv_data/{table_name}.csv')
    open_file.readline()
    cursor.copy_from(open_file, f'{table_name_lower}', sep=',')
    print("The data were recorded in the table")
    connect.commit()
    connect.close()
    open_file.close()
    print('Connection closed')


company_data = [
        ('PD', 1554940800), ('ZUO', 1523491200), ('PINS', 1555545600), ('ZM', 1555545600),
        ('PVL', 1320278400), ('DOCU', 1524787200), ('CLDR', 1493337600), ('RUN', 1438732800),
        ]


for comp in company_data:
    save_data_to_csv_file(f'{comp[0]}.csv', parser_csv(f'{comp[0]}', comp[1]))
    create_table_to_bd(f'{comp[0]}', connection_to_bd())
    saved_data_to_table(f'{comp[0]}', connection_to_bd())
    print('')


