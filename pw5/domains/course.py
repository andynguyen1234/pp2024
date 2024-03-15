class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

    def describe(self):
        print("Course ID: ", self.course_id)
        print("Course Name: ", self.name)
        print("Credit: ", self.credit)

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.name}, Credit: {self.credit}."
