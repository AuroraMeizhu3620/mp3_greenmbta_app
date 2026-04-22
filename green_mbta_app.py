from flask import Flask, render_template, request

from functions.geocode_transform import geocode_transform
from functions.nearest_stop import nearest_stop
from functions.get_air_quality import get_air_quality
from functions.interpret_aqi import interpret_aqi
from functions.results import results

app = Flask(__name__)

@app.route("/")
def home_form():
    return render_template("home_form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # 1. Get user input
    location = request.form["location"]

    print("User entered:", location)

    # 2. Call your pipeline function
    result = results(location)

    # 3. Handle errors
    if "error" in result:
        return result["error"]

    # 4. Send result to HTML template
    return render_template("result.html", result=result)  
    
if __name__ == "__main__":
    app.run(debug=True)