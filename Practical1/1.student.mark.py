# Input number of students in a class
def input_num_students():
    num_students = int(input("Number of students: "))
    return num_students

#Input student information: id, name, DoB
def input_student_info(num_students):
    student = {}
    for i in range(num_students):
        student_id = str(input("Student ID: "))
        name = str(input("Student Name: "))
        DoB = str(input("Date of Birth: "))
        student[student_id] = (name, DoB)
    return student

#Input number of courses
def input_num_courses():
    num_courses = int(input("Number of courses: "))
    return num_courses

#Input course information: id, name
def input_course_info(num_courses):
    course = {}
    for i in range(num_courses):
        course_id = str(input("Course ID: "))
        name = str(input("Course Name: "))
        course[course_id] = (name)
    return course

#Input marks for students
def input_student_marks(student, course):
    mark = {}
    course_id = input("Select a course ID: ")
    if course_id in course:
        print(f"Input marks for students in course '{course[course_id]}':")
        for student_id in student:
            score = float(input(f"Enter mark for {student[student_id][0]}: "))
            mark[student_id] = mark.get(student_id, {})
            mark[student_id].update({course_id: score})
        return mark
    else:
        print("Course not found")
        return {}

#Input marks for all courses
def input_marks_for_all_courses(student):
    mark = {}
    num_courses = input_num_courses()
    course_info = input_course_info(num_courses)
    for course_id in course_info:
        mark.update(input_student_marks(student, course_info))
    return mark
    
#List students
def list_students(student):
    print("List of students: ")
    for student_id, info in student.items():
        print(f"Student ID: {student_id}, Name: {info[0]}, DoB: {info[1]}")
    
#List courses
def list_courses(course):
    print("List of courses: ")
    for course_id, info in course.items():
        print(f"Course ID: {course_id}, Name: {info}")

#Show student marks for a given course
def show_student_marks(mark, student):
    course_id = input("Enter course ID to show student marks: ")
    if any(course_id in score for score in mark.values()):
        print(f"Student marks for course {course_id}: ")
        for student_id, score in mark.items():
            print(f"{student[student_id][0]}: {score[course_id]}")
    else:
        print("No marks available for the selected course")

#Main
if __name__ == "__main__":
    num_students = input_num_students()
    student_info = input_student_info(num_students)

    students_marks = input_marks_for_all_courses(student_info) 
    list_students(student_info)
    show_student_marks(students_marks, student_info)


        
    
