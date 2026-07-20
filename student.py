class Student:
    # creates a Student object
    def __init__(self, id, name, age, email, course_name, course_id):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.course_name = course_name
        self.course_id = course_id
        
    # converts the Student object into a dictionary so that it can be easily stored in a JSON format
    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'age' : self.age,
            'email' : self.email,
            'course_name' : self.course_name,
            'course_id' : self.course_id
        }
    
    # recreates a Student object from JSON data
    @staticmethod
    def from_dict(data):
        return Student(
            data['id'],
            data['name'],
            data['age'],
            data['email'],
            data['course_name'],
            data['course_id']
        )