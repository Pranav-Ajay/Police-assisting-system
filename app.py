from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd
import os


app = Flask(__name__)
CORS(app)

@app.route("/save_fir", methods=["POST"])
def save_fir():
    data = request.json

    file_path = "DELHI_MASTER_CRIME_DATASET_FINAL_CLEAN.csv"

    df = pd.DataFrame([data])

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, mode='w', header=True, index=False)

    return jsonify({"status": "saved"})


if __name__ == "__main__":
    app.run(debug=True)

