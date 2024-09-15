# db.py
import MySQLdb
def get_db_connection():
    connection = MySQLdb.connect(
        host='inst-bd-proyecto1.cxugamk8a6sf.us-east-2.rds.amazonaws.com',
        user='admin',
        passwd='C4rl0s99*',
        db='db_actividades'
    )
    return connection
