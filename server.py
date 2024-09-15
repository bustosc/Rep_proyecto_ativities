# server.py
from flask import Flask, request, render_template
from db import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    activity = request.form['activity']
    description = request.form['description']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO activities (activity, description) VALUES (%s, %s)", (activity, description))
        connection.commit()
        message = 'Activity added successfully!'
    except Exception as e:
        connection.rollback()
        message = f"Failed to add activity: {e}"
    finally:
        cursor.close()
        connection.close()
    
    return message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
