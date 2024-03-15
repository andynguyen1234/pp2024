import math
import numpy as np
import os
import shutil
import gzip
import pickle
from domains import Student, Course, Mark, School
import input as inn  # Update the import statement
import output as out

# Loading data from file or creating a new School instance
if os.path.exists('students.dat'):
    with gzip.open('students.dat', 'rb') as f:
        s = pickle.load(f)
else:
    s = School()
    inn.input_students(s)
    inn.input_courses(s)
    s.input_mark()
    with open('students.txt', 'w') as f:
        for student in s.student.values():
            f.write(str(student) + '\n')
    with open('courses.txt', 'w') as f:
        for course in s.course.values():
            f.write(str(course) + '\n')
    with open('marks.txt', 'w') as f:
        for mark in s.mark:
            f.write(str(mark) + '\n')
    with open('students.dat', 'wb') as f:
        with gzip.open(f, 'wb') as f_out:
            shutil.copyfileobj(f_out, f)
    with gzip.open('students.dat', 'wb') as f:
        pickle.dump(s, f)

# Displaying information using the output module
out.display_students(s.list_students())
out.display_courses(s.list_courses())
out.display_student_marks(s.show_student_marks())
out.display_sorted_students_by_gpa(s.display_sorted_students_by_gpa())
