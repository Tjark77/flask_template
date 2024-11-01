from flask import render_template, request
from flask.helpers import send_file
from __main__ import app
from flask.json import jsonify
import requests
import json
from models.test import Test

test_obj = Test()

# WEBSEITEN

# Zeigt die Basisseite an, hat keine weitere Funktion und kann entfernt werden
@app.route("/")
def index():
    return "Das hier ist die Indexseite. "

# Link zum Laden der HTML-Datei "test.html"
@app.route("/view_test")
def test_view():
    return render_template("test.html")

# Link zum Laden der HTML-Datei "test.html" in die HTML-Datei "master.html"
@app.route("/test")
def test():
    return render_template("master.html", site_name="view_test")

# BACKEND

# Get Backend
@app.route("/get")
async def get():
    return await test_obj.get()

# Post Backend
@app.route("/post", methods=["POST"])
async def post():
    my_json = request.get_json()
    return await test_obj.post(my_json)

# FRONTEND

# Link zum Laden des "BILD.jpg"
@app.route("/BILD.jpg")
def bild_jpg():
    return send_file("./static/BILD.jpg")

# Get Frontend
@app.route("/ajax/get")
def ajax_get():
    url = "http://127.0.0.1:5000/get"
    try:
        url_response = requests.get(url)
    except requests.ConnectionError:
        print("Fehler")
        return
    myjson = json.loads(url_response.text)
    return jsonify(myjson)

# Post Frontend
@app.route("/ajax/post", methods=["POST"])
def ajax_post():
    my_json = json.loads(request.get_data())
    response = requests.post("http://127.0.0.1:5000/post", json=my_json)
    return_json = json.loads(response.text)
    return jsonify(return_json)