from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from domains.school import School
from input import get_student_input, get_course_input, get_mark_input
from output import display_sorted_students_by_gpa

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
        credit = int(input("Course Credit: "))
        s.add_course(Course(course_id, name, credit))  # Adding credit attribute

    s.input_mark()
    s.list_students()
    s.list_courses()
    s.show_student_marks()
    s.display_sorted_students_by_gpa()  # Display sorted students by GPA

