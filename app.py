from flask import Flask, jsonify
from database import get_all_users, get_user

app = Flask(__name__)

@app.route("/")
def home():
    return "REST API demo"

# Uniform Interface
@app.route("/users")
def users():
    return jsonify(get_all_users())

@app.route("/users/<int:user_id>")
def user(user_id):
    u = get_user(user_id)
    if u:
        return jsonify(u)
    return {"error": "User not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)