# db.py
import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host='inst-bd-proyecto1.cxugamk8a6sf.us-east-2.rds.amazonaws.com',
        user='admin',
        password='C4rl0s99*',
        database='activities_db'
    )
    return connection

