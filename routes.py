from flask import request, jsonify
from helpers import delete_student_by_id, get_all_students, get_student_by_id, get_student_by_last_name, create_new_student, update_student_age_by_id, update_student_by_id

def register_routes(app, csv_file, fieldnames, required_fields, required_fields_age):

    @app.route("/")
    def hello():
        return "Привіт із Flask!"

    @app.route("/students/<int:student_id>", methods=["GET"])
    def get_student(student_id):
        student = get_student_by_id(student_id, csv_file)
        if not student:
            return jsonify({"error": "Student not found"}), 404
        return jsonify(student)

    @app.route("/students/lastname/<string:last_name>", methods=["GET"])
    def get_student_by_last_name_route(last_name):
        students = get_student_by_last_name(last_name, csv_file)
        if not students:
            return jsonify({"error": "Student(s) not found"}), 404
        return jsonify(students)

    @app.route("/students", methods=["GET"])
    def get_students():
        allStudents = get_all_students(csv_file)
        if not allStudents:
            return jsonify({"error": "Student(s) not found"}), 404
        return jsonify(allStudents)

    @app.route("/students", methods=["POST"])
    def create_student():
        data = request.json
        result = create_new_student(data, csv_file, fieldnames, required_fields)
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        return jsonify(result)

    @app.route("/students/<int:student_id>", methods=["PUT"])
    def update_student(student_id):
        data = request.json
        result = update_student_by_id(student_id, data, csv_file, fieldnames, required_fields)
        if isinstance(result, tuple):
            return jsonify(result[0]), result[1]
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        return jsonify(result)

    @app.route("/students/<int:student_id>", methods=["PATCH"])
    def update_student_age(student_id):
        data = request.json
        result = update_student_age_by_id(student_id, data, csv_file, fieldnames, required_fields_age)
        if isinstance(result, tuple):
            return jsonify(result[0]), result[1]
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        return jsonify(result)
    
    @app.route("/students/<int:student_id>", methods=["DELETE"])
    def delete_student(student_id):
        result = delete_student_by_id(student_id, csv_file, fieldnames)
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        return jsonify(result)