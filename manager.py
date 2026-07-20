from student import Student
from storage import read_data, write_data

class StudentManager:

    # loads students from student.json 
    def __init__(self):
        self.students = []

        data = read_data()
        for student_data in data:
            student = Student.from_dict(student_data)
            self.students.append(student)
    # saves current student list to the JSON file
    def save(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        write_data(data)
    # adds a new student and saves it to JSON file
    def add_student(self, student):
         # check for duplicate id
        for s in self.students:
            if s.id == student.id:
                raise ValueError(f"Student with id {student.id} already exists.")
             
        self.students.append(student)
        self.save()
        print(f"Student {student.name} added successfully.")
    # displays all students in the list
    def view_students(self):
        # check if there are any student in the list
        if not self.students:
            print("No students found.")
            return
        
        print("-------- List of Students ---------")

        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Email: {student.email}, Course Name: {student.course_name}, Course ID: {student.course_id}")

    # searches for a student by id and return the studen object if found
    def search_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None
    
    # deletes a student by id
    def delete_student(self, id):
        student = self.search_student(id)
        if student:
            self.students.remove(student)
            self.save()
            print(f"Student with id {id} deleted successfully.")
        else:
            print(f"Student with id {id} not found.")
            
    # uodates details of existing student 
    def update_student(self, id, name=None, age=None, email=None, course_name=None, course_id=None):
        student = self.search_student(id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if email:
                student.email = email
            if course_name:
                student.course_name = course_name
            if course_id:
                student.course_id = course_id
            
            self.save()
            print(f"Student with id {id} updated successfully.")
        else:
            print(f"Student with id {id} not found.")