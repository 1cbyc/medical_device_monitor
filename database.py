import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='your_host'
    )
    return conn
