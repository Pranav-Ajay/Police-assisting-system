from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root123",
    database="users"
)

@app.route("/users", methods=["GET"])
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT uid, post FROM users ORDER BY post")
    data = cursor.fetchall()
    return jsonify(data)


