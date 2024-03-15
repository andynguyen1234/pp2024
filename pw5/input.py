from domains.student import Student
from domains.course import Course

def input_students(school):
    num_students = int(input("Number of students: "))
    for _ in range(num_students):
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        DoB = input("Date of Birth: ")
        school.add_student(Student(student_id, name, DoB))

def input_courses(school):
    num_courses = int(input("Number of courses: "))
    for _ in range(num_courses):
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Course Credit: "))
        school.add_course(Course(course_id, name, credit))
