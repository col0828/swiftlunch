from flask import Flask, render_template, jsonify, request
import meal

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/meal1-api", methods=["GET", "POST"])
def meal1_api():
    if request.method == "GET":
        print("error")
    elif request.method == "POST":
        meals = meal.meal1()
        result = {}
        result["first"] = str("\n".join(meals[0])).split()
        # print(result['first'])
        return jsonify(result)


@app.route("/meal2-api", methods=["GET", "POST"])
def meal2_api():
    if request.method == "GET":
        print("error")
    elif request.method == "POST":
        meals = meal.meal1()
        result = {}
        result["second"] = str("\n".join(meals[1])).split()
        # print(result['first'])
        return jsonify(result)


@app.route("/meal3-api", methods=["GET", "POST"])
def meal3_api():
    if request.method == "GET":
        print("error")
    elif request.method == "POST":
        meals = meal.meal1()
        result = {}
        result["first"] = str("\n".join(meals[2])).split()
        # print(result['first'])
        return jsonify(result)


@app.route('/about')
def about():
    return 'About'
