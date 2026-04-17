import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2346",  # put your MySQL password here
        database="crime_db"
    )