import math

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
