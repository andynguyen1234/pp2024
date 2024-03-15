class Student:
    def __init__(self, student_id, name, DoB):
        self.student_id = student_id
        self.name = name
        self.DoB = DoB
    
    def describe(self):
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.name)
        print("Date of birth: ", self.DoB)
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, DoB: {self.DoB}."
