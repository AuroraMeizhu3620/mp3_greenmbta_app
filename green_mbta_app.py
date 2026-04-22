from flask import Flask, render_template, request
from functions.results import results
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")

@app.route("/")
def home_form():
    return render_template("home_form.html")

@app.route("/submit", methods=["POST"])
def submit():
    location = request.form["location"]
    result = results(location)

    if "error" in result:
        return result["error"]

    return render_template("result.html", result=result, mapbox_token=MAPBOX_TOKEN)

if __name__ == "__main__":
    app.run(debug=True)