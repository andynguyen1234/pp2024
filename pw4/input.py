from domains.student import Student
from domains.course import Course
from domains.mark import Mark

def get_student_input():
    student_id = input("Student ID: ")
    name = input("Student Name: ")
    dob = input("Date of Birth: ")
    return Student(student_id, name, dob)

def get_course_input():
    course_id = input("Course ID: ")
    name = input("Course Name: ")
    credit = int(input("Course Credit: "))
    return Course(course_id, name, credit)

def get_mark_input(student_id, course_id):
    score = float(input(f"Enter mark for student {student_id} in course {course_id}: "))
    return Mark(student_id, course_id, score)
