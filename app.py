from flask import Flask, jsonify
from database import students

app = Flask(__name__)

@app.route("/")
def home():
    return "Client-Server REST demo"

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)