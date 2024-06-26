from flask import Flask, render_template
import json
app = Flask(__name__)



@app.route("/")
def index():
    with open("database/VRoadDB.json", encoding="utf-8") as file:
        data=json.load(file)
    return render_template("index.html", players=data)

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    return render_template("signup_form.html")