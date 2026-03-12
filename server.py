from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensor_data = {
    "soil": 0,
    "temperature": 0,
    "humidity": 0,
    "rain": 0,
}

command = {
    "pump": "OFF",
}


def ai_logic(data):
    soil = data["soil"]
    temp = data["temperature"]
    rain = data["rain"]

    if rain == 1:
        command["pump"] = "OFF"
    elif soil < 35 and temp > 30:
        command["pump"] = "ON"
    elif soil < 40:
        command["pump"] = "ON"
    else:
        command["pump"] = "OFF"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sensor", methods=["POST"])
def sensor():
    data = request.json

    sensor_data["soil"] = data.get("soil", sensor_data["soil"])
    sensor_data["temperature"] = data.get("temperature", sensor_data["temperature"])
    sensor_data["humidity"] = data.get("humidity", sensor_data["humidity"])
    sensor_data["rain"] = data.get("rain", sensor_data["rain"])

    ai_logic(sensor_data)

    return jsonify(command)


@app.route("/command")
def get_command():
    return jsonify(command)


@app.route("/data")
def data():
    return jsonify(sensor_data)


@app.route("/pump", methods=["POST"])
def manual():
    data = request.json
    command["pump"] = data.get("pump", command["pump"])

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # Enable debug mode for auto-reload when templates or code change.
    # Remove debug=True in production.
    app.run(host="0.0.0.0", port=5000, debug=True)
