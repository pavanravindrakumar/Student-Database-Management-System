from file_handler import load_students, save_students
from utils import get_non_empty_input, get_valid_int

def add_student():
    students = load_students()

    roll = get_non_empty_input("Enter roll number: ")
    if any(s["roll"] == roll for s in students):
        print("Student with this roll number already exists.")
        return

    name = get_non_empty_input("Enter name: ")
    marks = get_valid_int("Enter marks: ")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return

    for s in students:
        print(
            f"Roll: {s['roll']} | "
            f"Name: {s['name']} | "
            f"Marks: {s['marks']}"
        )


def search_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student found:")
            print(s)
            return

    print("Student not found.")


def update_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to update: ")

    for s in students:
        if s["roll"] == roll:
            s["marks"] = get_valid_int("Enter new marks: ")
            save_students(students)
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to delete: ")

    new_students = [s for s in students if s["roll"] != roll]

    if len(new_students) == len(students):
        print("Student not found.")
        return

    save_students(new_students)
    print("Student deleted successfully.")


def sort_students_by_marks():
    students = load_students()
    students.sort(key=lambda s: int(s["marks"]), reverse=True)

    print("\nStudents sorted by marks (high → low):")
    for s in students:
        print(s)