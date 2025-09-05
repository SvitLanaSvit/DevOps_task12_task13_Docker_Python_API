
from flask import Flask, request, jsonify
from routes import register_routes
from helpers import ensure_csv_exists

CSV_FILE = "resources/students.csv"
FIELDNAMES = ["id", "first_name", "last_name", "age"]
REQUIRED_FIELDS = ["first_name", "last_name", "age"]
REQUIRED_FIELD_AGE = ["age"]

ENDPOINTS = {
    "get_students": "/students",
    "get_student_by_id": "/students/{sid}",
    "get_student_by_last_name": "/students/lastname/{last_name}",
    "create_student": "/students",
    "update_student": "/students/{sid}",
    "update_student_age": "/students/age/{sid}",
    "delete_student": "/students/{sid}"
}

app = Flask(__name__)
ensure_csv_exists(CSV_FILE, FIELDNAMES)
register_routes(app, CSV_FILE, FIELDNAMES, REQUIRED_FIELDS, REQUIRED_FIELD_AGE)

if __name__ == "__main__":
    app.run(debug=True)