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
        return self.student.values()
    
    def list_courses(self):
        return self.course.values()
    
    def show_student_marks(self):
        student_marks = []
        for student_id in self.student:
            marks = []
            total_gpa = 0
            total_courses = 0
            for course_id in self.course:
                for mark in self.mark:
                    if mark.student_id == student_id and mark.course_id == course_id:
                        marks.append((self.course[course_id].name, mark.score))
                        total_gpa += mark.score
                        total_courses += 1
            if total_courses > 0:
                average_gpa = total_gpa / total_courses
                student_marks.append((student_id, self.student[student_id].name, marks, average_gpa))
            else:
                student_marks.append((student_id, self.student[student_id].name, "No marks available"))
        return student_marks

    def display_sorted_students_by_gpa(self):
        sorted_students = self.sort_students_by_gpa()
        return [self.student[id] for id in sorted_students]

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
        return [id for id, _ in sorted(student_gpa.items(), key=lambda item: item[1], reverse=True)]
