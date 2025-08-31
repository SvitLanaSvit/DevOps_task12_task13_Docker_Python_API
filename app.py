
from flask import Flask, request, jsonify
from routes import register_routes
from helpers import ensure_csv_exists

CSV_FILE = "students.csv"
FIELDNAMES = ["id", "first_name", "last_name", "age"]
REQUIRED_FIELDS = ["first_name", "last_name", "age"]
REQUIRED_FIELDS_AGE = ["age"]

ENDPOINTS = {
    "students": "/students",
    "student_by_id": "/students/<int:sid>"
}

app = Flask(__name__)
ensure_csv_exists(CSV_FILE, FIELDNAMES)
register_routes(app, CSV_FILE, FIELDNAMES, REQUIRED_FIELDS, REQUIRED_FIELDS_AGE)

if __name__ == "__main__":
    app.run(debug=True)