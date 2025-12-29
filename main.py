from students_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    sort_students_by_marks
)

def menu():
    while True:
        print("\n--- Student Database Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort by Marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            sort_students_by_marks()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()