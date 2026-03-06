from flask import Flask, jsonify, request, make_response
import database

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    response = make_response(jsonify(database.get_all_users()))
    response.headers["Cache-Control"] = "public, max-age=60"
    return response


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = database.get_user(user_id)

    if user:
        response = make_response(jsonify(user))
        response.headers["Cache-Control"] = "public, max-age=60"
        return response

    return {"error": "User not found"}, 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    new_user = {
        "id": len(database.users) + 1,
        "name": data["name"]
    }

    database.users.append(new_user)

    return jsonify(new_user)


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    for u in database.users:
        if u["id"] == user_id:
            database.users.remove(u)
            return {"message": "deleted"}

    return {"error": "User not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)