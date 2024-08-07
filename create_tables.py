import os
import psycopg2
from dotenv import load_dotenv

# will load environment variables from .env file
load_dotenv()


def connect_db():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT'))  # make sure port is an integer
    )
    return conn


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # to create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS device_data (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP,
        heart_rate INTEGER,
        device_id INTEGER,
        status VARCHAR(50)
    )
    """)
    conn.commit()

    # to insert sample data
    cursor.execute("""
    INSERT INTO device_data (timestamp, heart_rate, device_id, status) VALUES
    ('2024-01-01 00:00:00', 70, 1, 'active'),
    ('2024-01-01 01:00:00', 75, 1, 'active'),
    ('2024-01-01 02:00:00', 72, 1, 'active')
    """)
    conn.commit()

    cursor.close()
    conn.close()
    print("Table created and sample data inserted successfully.")


if __name__ == '__main__':
    create_table()
