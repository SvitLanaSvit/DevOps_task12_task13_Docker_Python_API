import requests
from app import ENDPOINTS
from entity.Student import Student
import os

BASE_URL = "http://127.0.0.1:5000"

# 1. Отримати всіх існуючих студентів (GET)
def get_students(filepath):
    url = f"{BASE_URL}{ENDPOINTS['get_students']}"
    job = f"GET All Students"
    response = requests.get(url)
    print("GET /students:", response.status_code)
    print(response.json())
    write_result_to_file(job, filepath, url, response.text)

def get_student_by_id(student_id: int, filepath: str):
    url = f"{BASE_URL}{ENDPOINTS['get_student_by_id'].format(sid=student_id)}"
    job = f"GET Student by ID: "
    response = requests.get(url)
    print(f"GET /students/{student_id}:", response.status_code)
    try:
        print(response.json())
        write_result_to_file(job, filepath, url, response.text)
    except Exception:
        print(response.text)

def create_student(student: Student, filepath: str):
    url = f"{BASE_URL}{ENDPOINTS['create_student']}"
    job = f"POST Create Student: "
    response = requests.post(url, json=student.to_dict())
    print("POST /students:", response.status_code)
    print(response.json())
    write_result_to_file(job, filepath, url, response.text)

def update_age_student(student_id: int, new_age: int, filepath: str):
    url = f"{BASE_URL}{ENDPOINTS['update_student_age'].format(sid=student_id)}"
    job = f"PATCH Update Student Age: "
    response = requests.patch(url, json={"age": new_age})
    print(f"PATCH /students/age/{student_id}:", response.status_code)
    print(response.json())
    write_result_to_file(job, filepath, url, response.text)

def update_student(student_id: int, first_name: str, last_name: str, age: int, filepath: str):
    url = f"{BASE_URL}{ENDPOINTS['update_student'].format(sid=student_id)}"
    job = f"PUT Update Student: "
    response = requests.put(url, json={
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    })
    print(f"PUT /students/{student_id}:", response.status_code)
    print(response.json())
    write_result_to_file(job, filepath, url, response.text)

def delete_student(student_id: int, filepath: str):
    url = f"{BASE_URL}{ENDPOINTS['delete_student'].format(sid=student_id)}"
    job = f"DELETE Student: "
    response = requests.delete(url)
    print(f"DELETE /students/{student_id}:", response.status_code)
    print(response.json())
    write_result_to_file(job, filepath, url, response.text)

def write_result_to_file(job, filepath: str, url: str, result: str):
    ensure_results_exists(filepath)
    with open(filepath, "a", encoding="utf-8") as f:
        original_stdout = os.sys.stdout
        os.sys.stdout = f
        f.write(f"Job: {job} :")
        f.write(f"URL: {url}\n")
        f.write(f"Result: {result}\n")
        f.write("\n")
        os.sys.stdout = original_stdout

def ensure_results_exists(file_path: str) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            pass


if __name__ == "__main__":
    filepath = "results.txt"

    # 1
    get_students(filepath)
    print(f"-----\n")

    # 2 #create the three new students
    create_student(Student(None, "John", "Doe", 22), filepath)
    create_student(Student(None, "Jane", "Smith", 23), filepath)
    create_student(Student(None, "Emily", "Johnson", 24), filepath)
    print(f"-----\n")

    # 3
    get_students(filepath)
    print(f"-----\n")

    # 4
    update_age_student(2, 25, filepath)  # Update age for student with id=2
    print(f"-----\n")

    # 5
    get_student_by_id(2, filepath)
    print(f"-----\n")

    #6 Update the fist name, last name and the age of the third student (PUT)
    update_student(3, "Emma", "Williams", 27, filepath)
    print(f"-----\n")

    #7 Retrieve information about the third student (GET)
    get_student_by_id(3, filepath)
    print(f"-----\n")

    # 8 Retrieve all existing students (GET).
    get_students(filepath)
    print(f"-----\n")

    #9 Delete the first user (DELETE).
    delete_student(1, filepath)
    print(f"-----\n")

    #10 Retrieve all existing students (GET).
    get_students(filepath)
