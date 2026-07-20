from student import Student 
from manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            course_id = input("Enter course ID: ")

            student = Student(id, name, age, email, course_name, course_id)
            try:
                manager.add_student(student)
            except ValueError as e:
                print(e)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            id = input("Enter student ID to search: ")
            student = manager.search_student(id)
            if student:
                print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Email: {student.email}, Course Name: {student.course_name}, Course ID: {student.course_id}")
            else:
                print(f"Student with id {id} not found.")

        elif choice == '4':
            id = input("Enter student ID to delete: ")
            manager.delete_student(id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()