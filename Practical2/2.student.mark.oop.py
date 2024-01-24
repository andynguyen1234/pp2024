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

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
    
    def describe(self):
        print("Course ID: ", self.course_id)
        print("Course Name: ", self.name)
    
    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.name}."
    
class Mark:
    def __init__(self, student_id, course_id, score):
        self.student_id = student_id
        self.course_id = course_id
        self.score = score

    def describe(self):
        print("Student ID: ", self.student_id)
        print("Course ID: ", self.course_id)
        print("Score: ", self.score)
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Score: {self.score}."
    

class School:
    def __init__(self):
        self.student = {}
        self.course = {}
        self.mark = []

    def add_student(self, student):
        self.student[student.student_id] = student

    def add_course(self, course):
        self.course[course.course_id] = course

    def input_mark(self):
        course_id = input("Select a Course ID: ")
        if course_id in self.course:
            print(f"Input marks for students in course: '{self.course[course_id].name}':")
            for student_id, student in self.student.items():
                score = float(input(f"Enter mark for {student.name}: "))
                self.mark.append(Mark(student_id, course_id, score))
        else:
            print("Course not found")
    
    def input_mark(self):
        for course_id in self.course:
            print(f"Input marks for students in course: '{self.course[course_id].name}':")
            for student_id, student in self.student.items():
                score = float(input(f"Enter mark for {student.name} in course {self.course[course_id].name}: "))
                self.mark.append(Mark(student_id, course_id, score))


    def list_students(self):
        print("List of students: ")
        for student in self.student.values():
            print(student)
    
    def list_courses(self):
        print("List of courses: ")
        for course in self.course.values():
            print(course)
    
    def show_student_marks(self):
        course_id = input("Enter course ID to show student marks: ")
        print(f"Student marks for course {course_id}:")
        for mark in self.mark:
            if mark.course_id == course_id:
                print(mark)

#Main
if __name__ == "__main__":
    s = School()
    num_students = int(input("Number of students: "))
    for _ in range(num_students):
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        DoB = input("Date of Birth: ")
        s.add_student(Student(student_id, name, DoB))
    
    num_courses = int(input("Number of courses: "))
    for _ in range(num_courses):
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        s.add_course(Course(course_id, name))
    
    s.input_mark()
    s.list_students()
    s.list_courses()
    s.show_student_marks()





    




        
