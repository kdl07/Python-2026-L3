import numpy as np
import curses

def list_courses(courses):
    if not courses:
        print("No courses available.")
        return
    print("--- Course List ---")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}, Credits: {course['credits']}")

def list_students(students):
    if not students:
        print("No students available.")
        return
    print("--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def student_marks(courses, students, marks_list):
    if not courses or not students or not marks_list:
        print("Missing data or marks have not been entered yet.")
        return
    list_courses(courses)
    course_id = input("Enter Course ID to view marks: ")
    
    target_marks = next((m for m in marks_list if m['course_id'] == course_id), None)
    if not target_marks:
        print("No marks found for this course.")
        return
        
    print(f"--- Marks for Course ID: {course_id} ---")
    for student in students:
        score = target_marks["grades"].get(student['id'], "N/A")
        print(f"Student: {student['name']} (ID: {student['id']}) - Mark: {score}")

def calculate_gpa(student_id, courses, marks_list):
    marks = []
    credits = []
    for m in marks_list:
        if student_id in m["grades"]:
            course_id = m["course_id"]
            course = next((c for c in courses if c['id'] == course_id), None)
            if course:
                marks.append(m["grades"][student_id])
                credits.append(course['credits'])
    
    if not marks or sum(credits) == 0:
        return 0.0
    
    # Use numpy arrays for weighted sum calculation
    marks_arr = np.array(marks)
    credits_arr = np.array(credits)
    gpa = np.dot(marks_arr, credits_arr) / np.sum(credits_arr)
    return round(gpa, 2)

def sort_students_by_gpa(students, courses, marks_list):
    if not students or not courses or not marks_list:
        print("Missing student, course, or marks data to calculate GPA.")
        return

    student_gpas = []
    for student in students:
        gpa = calculate_gpa(student['id'], courses, marks_list)
        student_gpas.append((student, gpa))
    
    # Sort descending by GPA
    student_gpas.sort(key=lambda x: x[1], reverse=True)
    
    print("\n--- Students Sorted by GPA (Descending) ---")
    for student, gpa in student_gpas:
        print(f"ID: {student['id']}, Name: {student['name']}, GPA: {gpa}")