import curses

def display_sorted_students_by_gpa(sorted_students, student_data):
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.addstr(0, 0, "List of students sorted by GPA:", curses.color_pair(1))

    for idx, student_id in enumerate(sorted_students):
        student = student_data[student_id]  # Access the student data from the provided dictionary
        gpa = calculate_gpa(student_id, student_data)
        stdscr.addstr(idx + 2, 0, f"{student.name} - GPA: {gpa:.2f}")

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