import curses

def display_students(students):
    print("List of students: ")
    for student in students:
        print(student)

def display_courses(courses):
    print("List of courses: ")
    for course in courses:
        print(course)

def display_student_marks(student_marks):
    print("Student marks for all courses:")
    for student_mark in student_marks:
        print(student_mark)

def display_sorted_students_by_gpa(sorted_students):
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.addstr(0, 0, "List of students sorted by GPA:", curses.color_pair(1))

    for idx, student in enumerate(sorted_students):
        stdscr.addstr(idx+2, 0, f"{student.name} - GPA: {student.gpa:.2f}")
