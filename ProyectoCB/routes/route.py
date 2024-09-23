from flask import render_template, request, jsonify
from server import app
from database.db import *
from controllers.admin_s3 import *

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/register_page')
def register_page():
    return render_template("register_activity.html")

@app.route('/consult_page')
def consult_page():
    return render_template("consult_activity.html")

@app.route('/register_activity', methods=["post"])
def register_activity():
    data = request.form
    file = request.files
    activity, description = data["activity"], data["description"]
    image = file["document"]
    insert(activity, description)
    session_s3 = connectionS3()
    image_path, image_name = save_file(activity, image)    
    upload_file_s3(session_s3, image_path, image_name)
    
    return "Actividad añadida"

@app.route('/consult_activity', methods=["post"])
def consult_activity():
    activity_id = request.get_json()
    result = consult(activity_id)
    if result:
        activity_name = result[0][1]
        description = result[0][2]
        image_url = get_image_url(activity_name)
        resp_data = {
            'activity_name': activity_name,
            'description': description,
            'image_url': image_url
        }
        return jsonify(resp_data)
    else:
        return jsonify({"error": "Actividad no encontrada"}), 404

