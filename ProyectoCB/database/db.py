import pymysql

host = 'inst-bd-proyecto1.cxugamk8a6sf.us-east-2.rds.amazonaws.com'
user = 'admin'
password = 'C4rl0s99*'
database = 'activities_db'

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as err:
        print("Error", err)
        return None

def insert(activity, description):
    try:
        instruction = f"INSERT INTO activities (activity, description) VALUES ('{activity}', '{description}');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("Actividad añadida")
    except Exception as err:
        print("Error", err)
        return None

def consult(activity_id):
    try:
        instruction = f"SELECT * FROM activities WHERE id={activity_id};"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Error", err)
        return None
