from flask import Flask, jsonify, request
import database

app = Flask(__name__)

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(database.get_all_users())


# GET one user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = database.get_user(user_id)

    if user:
        return jsonify(user)

    return {"error": "User not found"}, 404


# POST create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    new_user = {
        "id": len(database.users) + 1,
        "name": data["name"]
    }

    database.users.append(new_user)

    return jsonify(new_user)


# DELETE user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    for u in database.users:
        if u["id"] == user_id:
            database.users.remove(u)
            return {"message": "deleted"}

    return {"error": "User not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)