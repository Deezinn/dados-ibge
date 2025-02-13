import psycopg2
from config.database import database_info

def load():

    conn = psycopg2.connect(host=database_info['host'],
                            port=database_info['port'],
                            user=database_info['user'],
                            password=database_info['password'],
                            dbname=database_info['dbname'],)
    print('conectou')

    cur = conn.cursor()

    # aqui ficará o insert dos dados tratados em csv

    cur.close()
    conn.close()
    print('desconectou do banco')

print(database_info)

if __name__ == "__main__":
    load()
