from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []


@app.route("/log", methods=["POST"])
def receive_log():

    data = request.json

    logs.append(data)

    print("Log received:", data)

    return jsonify({"status": "received"})


@app.route("/logs")
def get_logs():

    return jsonify(logs)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
