from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# -------- DATABASE CONNECTION --------
db = mysql.connector.connect(
    host="localhost",       # your server
    user="root",            # your MySQL username
    password="YOUR_PASSWORD",
    database="police_db"    # your existing database name
)

# -------- SAVE DATA FROM FORM --------
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO officers (name, email) VALUES (%s, %s)",
        (name, email)
    )
    db.commit()

    return jsonify({"message": "Data saved successfully!"})

# -------- RUN SERVER --------
if __name__ == "__main__":
    app.run(debug=True)
