from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        goal = request.form.get("goal")
        # You’ll integrate Gemini and DB here
        return render_template("result.html", goal=goal)
    return render_template("index.html")

