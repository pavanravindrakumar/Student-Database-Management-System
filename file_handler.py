import csv
import os

FILE_PATH = "data/students.csv"

def ensure_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["roll", "name", "marks"])

def load_students():
    ensure_file()
    with open(FILE_PATH, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_students(students):
    ensure_file()
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["roll", "name", "marks"]
        )
        writer.writeheader()
        writer.writerows(students)