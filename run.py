from flask import Flask, render_template, jsonify, url_for, request
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
        data = json.load(file)
        
    # Obtener la lista de jugadores
    players = data.get("Players", [])
    
    # Buscar datos del jugador específico
    player_info = None
    for player in players:
        if player["Player"].lower() == slug.lower():
            player_info = player
            break

    player_info["image_url"] = url_for('static', filename='{}.webp'.format(slug.lower()))  
    
    if player_info:
        return render_template("player_data.html", player=player_info)
    else:
        return jsonify({"error": "Jugador no encontrado"}), 404


@app.route("/")
def index():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("index.html", players=data)

@app.route("/WIP-Calculator/")
def wip_calculator():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("dynamic_calculator_NotFullyFunctional.html", players=data)

@app.route('/about_us/')
def about_us():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("about_us.html", players=data)

@app.route('/get_boots_data')
def get_boots_data():
    with open('database/VRoadDB.json') as f:
        data = json.load(f)
    return jsonify(data)