import math
import curses
import numpy as np

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
    def __init__(self, course_id, name, credit):  # Include the credit attribute in the constructor
        self.course_id = course_id
        self.name = name
        self.credit = credit  # Assign the credit attribute

    def describe(self):
        print("Course ID: ", self.course_id)
        print("Course Name: ", self.name)
        print("Credit: ", self.credit)  # Include credit in the description

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.name}, Credit: {self.credit}."

    
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
    
    def get_score(self):
        return math.floor(self.score * 10) / 10 
    

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
     print("Student marks for all courses:")
     for student_id in self.student:
        print(f"Student ID: {student_id}, Name: {self.student[student_id].name}")
        total_gpa = 0
        total_courses = 0
        for course_id in self.course:
            for mark in self.mark:
                if mark.student_id == student_id and mark.course_id == course_id:
                    print(f"Course: {self.course[course_id].name}, Mark: {mark.score}")
                    total_gpa += mark.score
                    total_courses += 1
        if total_courses > 0:
            average_gpa = total_gpa / total_courses
            print(f"Average GPA: {average_gpa:.2f}")
        else:
            print("No marks available")

    def display_sorted_students_by_gpa(self):
        sorted_students = self.sort_students_by_gpa()
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        stdscr.addstr(0, 0, "List of students sorted by GPA:", curses.color_pair(1))

        for idx, student_id in enumerate(sorted_students):
            student = self.student[student_id]
            gpa = self.calculate_gpa(student_id)
            stdscr.addstr(idx+2, 0, f"{student.name} - GPA: {gpa:.2f}")

    def calculate_gpa(self, student_id):
        total_credit = 0
        weighted_sum = 0
        for mark in self.mark:
            if mark.student_id == student_id:
                course_credit = self.course[mark.course_id].credit
                total_credit += course_credit
                weighted_sum += (course_credit * mark.score)
        if total_credit == 0:
            return 0
        return weighted_sum / total_credit

    def sort_students_by_gpa(self):
        student_gpa = {}
        for student_id in self.student.keys():
            student_gpa[student_id] = self.calculate_gpa(student_id)
        sorted_students = [id for id, _ in sorted(student_gpa.items(), key=lambda item: item[1], reverse=True)]
        return sorted_students


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
        credit = int(input("Course Credit: "))
        s.add_course(Course(course_id, name, credit))  # Adding credit attribute

    s.input_mark()
    s.list_students()
    s.list_courses()
    s.show_student_marks()
    s.display_sorted_students_by_gpa()  # Display sorted students by GPA






    




        
