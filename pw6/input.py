import math
from domains.student import Student
from domains.course import Course

def save_students(students):
    with open("students.txt", "w") as file:
        for s in students:
            file.write(f" Student's ID: {s['id']}, Student's name: {s['name']}, Student's DOB: {s['dob']}\n")

def save_courses(courses):
    with open("courses.txt", "w") as file:
        for c in courses:
            file.write(f"Course ID: {c['id']}, Course name: {c['name']}, Course credits: {c['credits']}\n")

def save_marks(marks_list):
    with open("marks.txt", "w") as file:
        for m in marks_list:
            course_id = m["course_id"]
            for student_id, mark in m["grades"].items():
                file.write(f"Course ID: {course_id}, Student ID: {student_id}, Student's mark: {mark}\n")
    



def number_of_students():
    return int(input("Enter number of students in the class: "))

def student_info(n):
    students = [] 
    for i in range(n):
        print(f"Enter info for student {i+1}:")
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth (Dob): ")
        students.append({"id": student_id, "name": name, "dob": dob})

    save_students(students)
    return students

def number_of_courses():
    return int(input("Enter number of courses: "))

def course_info(n):
    courses = []
    for i in range(n):
        print(f"Enter info for course {i+1}:")
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Course Credits: ")) 
        courses.append({"id": course_id, "name": name, "credits": credits})
    save_courses(courses) # Save 
    return courses

def input_marks(students, courses, marks_list):
    if not students or not courses:
        print("Please enter both students and courses first.") 
        return [] # Empty list if no student and/or course found
    
    course_id = input("Enter Course ID to input marks: ")
    # Verify course existence
    selected_course = next((c for c in courses if c['id'] == course_id), None) # Find/verify valid course
    if not selected_course:
        print("Course ID not found.")
        return []

    course_marks = {"course_id": course_id, "grades": {}} # Store the grades for this specific course
    print(f"Entering marks for course: {selected_course['name']}")
    for student in students: # Loop inputs
        raw_mark = float(input(f"Mark for {student['name']} (ID: {student['id']}): "))
        # Use math.floor to round down to 1-digit decimal
        mark = math.floor(raw_mark * 10) / 10
        course_marks["grades"][student['id']] = mark
    marks_list.append(course_marks)
    
    save_marks(marks_list)
    return course_marks