import curses
from domains.mark import Mark

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