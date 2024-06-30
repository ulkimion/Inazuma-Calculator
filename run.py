from flask import Flask, render_template
import json
app = Flask(__name__)



@app.route("/show_characters/")
def show_characters():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("show_characters.html", players=data)

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/player/<string:slug>/")
def player_data(slug):
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("player_data.html", player=data, slug_title=slug, content=slug)

@app.route("/")
def index():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("index.html", players=data)