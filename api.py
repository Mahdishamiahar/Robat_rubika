
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/users")
def get_users():
    with open("vipzexnet_db.json", "r") as f:
        data = json.load(f)
    out = {}
    for user in set(data["scores"].keys()) | set(data["warnings"].keys()):
        out[user] = {
            "score": data["scores"].get(user, 0),
            "warn": data["warnings"].get(user, 0)
        }
    return jsonify(out)

@app.route("/api/warn/<user>")
def warn_user(user):
    with open("vipzexnet_db.json", "r") as f:
        data = json.load(f)
    data["warnings"][user] = data["warnings"].get(user, 0) + 1
    with open("vipzexnet_db.json", "w") as f:
        json.dump(data, f)
    return "OK"

@app.route("/api/ban/<user>")
def ban_user(user):
    with open("vipzexnet_db.json", "r") as f:
        data = json.load(f)
    data["warnings"].pop(user, None)
    data["scores"].pop(user, None)
    with open("vipzexnet_db.json", "w") as f:
        json.dump(data, f)
    return "OK"

if __name__ == "__main__":
    app.run()
