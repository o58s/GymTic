import mysql.connector 
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

try:
    connection = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
    )

    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT VERSION();')
        db_version = cursor.fetchone()
        
except Error as e:
    print(f"Error while connecting to MySQL: {e}")

