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
    print(f"Student '{name}' added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return

    for s in students:
        display_student(s)

def display_student(student):
    print("-" * 20)
    print(f"Roll   : {student['roll']}")
    print(f"Name   : {student['name'].title()}")
    print(f"Marks  : {student['marks']}")
    print("-" * 20)

    
def search_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student found:")
            display_student(s)
            return

    print("Student not found.")


def update_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:")
            display_student(student)

            new_marks = get_valid_int("Enter new marks (0-100): ")

            confirm = input(
                f"Confirm update marks for '{student['name']}' to {new_marks}? (y/n): "
            )

            if confirm.lower() != 'y':
                print("Update cancelled.")
                return

            student["marks"] = new_marks
            save_students(students)
            print(f"Student '{student['name']}' updated successfully.")
            return

    print("Student not found.")


def delete_student():
    students = load_students()
    roll = get_non_empty_input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            print("Student found:")
            display_student(student)

            confirm = input(
                f"Are you sure you want to delete student '{student['name']}'? (y/n): "
            )

            if confirm.lower() != 'y':
                print("Delete operation cancelled.")
                return

            students.remove(student)
            save_students(students)
            print(f"Student '{student['name']} deleted successfully.")
            return

    print("Student not found.")

def sort_students_by_marks():
    students = load_students()
    students.sort(key=lambda s: int(s["marks"]), reverse=True)

    print("\nStudents sorted by marks (high → low):")
    for s in students:
        print(s)

def export_to_csv():
    students = load_students()
    save_students(students)
    print("Students exported to CSV successfully.")
