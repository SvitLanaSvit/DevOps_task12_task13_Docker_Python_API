import os
import csv
import logging

def ensure_csv_exists(csv_file, fieldnames):
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

def get_student_by_id(student_id, csv_file):
    if os.path.exists(csv_file):
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["id"] == str(student_id):
                    return row
    return None

def get_student_by_last_name(last_name, csv_file):
    students = []
    if os.path.exists(csv_file):
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["last_name"].strip().lower() == last_name.strip().lower():
                    students.append(row)
    return students

def get_all_students(csv_file):
    students = []
    if os.path.exists(csv_file):
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if any(row.values()):  # skip empty rows
                    students.append(row)
    return students

def validate_fields(data, fieldnames, required_fields):
    missing = [field for field in required_fields if not data.get(field)]
    extra = [field for field in data.keys() if field not in fieldnames]
    if missing:
        logging.error(f"Required fields are missing: {', '.join(missing)}")
        return {"error": f"Required fields are missing: {', '.join(missing)}"}
    if extra:
        logging.error(f"Invalid fields: {', '.join(extra)}")
        return {"error": f"Invalid fields: {', '.join(extra)}"}
    return None

def create_new_student(data, csv_file, fieldnames, required_fields):
    """Create a new student record in the CSV file. If id is not provided or empty, auto-increment it. If id exists, return error."""
    error = validate_fields(data, fieldnames, required_fields)
    if error:
        return error
    id_provided = data.get("id")
    id_exists = False
    max_id = 0
    if os.path.exists(csv_file):
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row_id = int(row["id"])
                    if row_id > max_id:
                        max_id = row_id
                    if id_provided and str(row_id) == str(id_provided):
                        id_exists = True
                except (ValueError, TypeError):
                    continue
    if id_provided:
        if id_exists:
            logging.error(f"Student with id {id_provided} already exists.")
            return {"error": f"Student with id {id_provided} already exists."}
        data["id"] = str(id_provided)
    else:
        data["id"] = str(max_id + 1)
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)
    return data

def update_student_by_id(student_id, data, csv_file, fieldnames, required_fields):
    error = validate_fields(data, fieldnames, required_fields)
    if error:
        return error
    student = get_student_by_id(student_id, csv_file)
    if not student:
        logging.error(f"Student by id {student_id} not found")
        return {"error": f"Student by id {student_id} not found"}, 404
    students = get_all_students(csv_file)
    updated = False
    for i, s in enumerate(students):
        if s["id"] == str(student_id):
            for key in fieldnames:
                if key in data and key != "id":
                    s[key] = data[key]
            students[i] = s
            updated = True
            break
    if not updated:
        logging.error(f"Student by id {student_id} not found")
        return {"error": f"Student by id {student_id} not found"}, 404
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    return s

def update_student_age_by_id(student_id, data, csv_file, fieldnames, required_field_age):
    error = validate_fields(data, fieldnames, required_field_age)
    if error:
        return error
    students = get_all_students(csv_file)
    for i, s in enumerate(students):
        if s["id"] == str(student_id):
            s["age"] = data.get("age")
            students[i] = s
            break
    else:
        logging.error(f"Student by id {student_id} not found")
        return {"error": f"Student by id {student_id} not found"}, 404
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    return s

def delete_student_by_id(student_id, csv_file, fieldnames):
    student = get_student_by_id(student_id, csv_file)
    if not student:
        return {"error": f"Student by id {student_id} not found"}, 404
    students = get_all_students(csv_file)
    students = [student for student in students if student["id"] != str(student_id)]
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
    return {"message": "Student deleted successfully"}