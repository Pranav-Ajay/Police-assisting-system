from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="YOUR_PASSWORD",
    database="police_db"    
)

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

if __name__ == "__main__":
    app.run(debug=True)
