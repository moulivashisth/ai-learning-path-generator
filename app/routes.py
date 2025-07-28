from flask import Blueprint, render_template, request
from .gemini_api import generate_learning_path
from .db import goals_collection  # Only if you're storing results in MongoDB
import json
import re
from flask import jsonify
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

def clean_json_response(raw_text):
    """
    Remove Markdown formatting like ```json ... ``` and return parsed JSON.
    """
    try:
        # Remove ```json ... ``` if present
        cleaned = re.sub(r"^```(?:json)?|```$", "", raw_text.strip(), flags=re.MULTILINE).strip()
        return json.loads(cleaned)
    except Exception as e:
        raise ValueError(f"Failed to parse JSON: {e}")

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        goal_text = request.form.get("goal")

        # Call Gemini
        raw_result = generate_learning_path(goal_text)

        # Attempt to clean and parse response
        try:
            steps = clean_json_response(raw_result)
        except Exception as e:
            steps = []
            return render_template("result.html", goal=goal_text, steps=None, raw_output=raw_result, error=str(e))

        for step in steps:
            step["completed"] = False

        goals_collection.insert_one({
            "goal": goal_text,
            "learning_path": steps
        })

        return render_template("result.html", goal=goal_text, steps=steps)

    return render_template("index.html")

@main.route("/toggle_step", methods=["POST"])
def toggle_step():
    from .db import goals_collection
    data = request.json
    goal = goals_collection.find_one({"goal": data["goal"]})

    if not goal:
        return jsonify({"success": False, "error": "Goal not found"})

    # Find the step index and toggle it
    steps = goal["learning_path"]
    step_index = int(data["step_index"])
    steps[step_index]["completed"] = not steps[step_index].get("completed", False)

    # Update in MongoDB
    goals_collection.update_one(
        {"goal": data["goal"]},
        {"$set": {"learning_path": steps}}
    )

    return jsonify({"success": True})

@main.route("/history")
def view_history():
    from .db import goals_collection
    goals = list(goals_collection.find({}, {"_id": 0}))  # exclude Mongo _id for clean display
    return render_template("history.html", goals=goals)

@main.route("/delete_goal", methods=["POST"])
def delete_goal():
    from .db import goals_collection
    data = request.json
    goal_text = data.get("goal")
    if goal_text:
        result = goals_collection.delete_one({"goal": goal_text})
        return jsonify({"success": result.deleted_count == 1})
    return jsonify({"success": False, "error": "Goal not found"})

