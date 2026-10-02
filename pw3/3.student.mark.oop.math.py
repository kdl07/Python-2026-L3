# Input: number of students, student's info, number of courses, course info, list of courses
# Output: display list of courses, list of students
# Then store scores into courses and set to students
import math
import numpy as np
import curses

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
    return courses

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

# --- Needs further explanation ---
# First check if students and/or the courses are available or not
# Then store the results into course_marks
# Finally assign to student then store as mark
def input_marks(students, courses):
    if not students or not courses:
        print("Please enter both students and courses first.") 
        return [] # Empty list if no student and/or course found
    
    list_courses(courses) # Access all available courses
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
        
    return course_marks

# Define a function to display students' scores
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

def main():
    students = []
    courses = []
    marks_list = [] 

    while True:
        print("\n--- Student Management System ---")
        print("1. Input students info")
        print("2. Input courses info")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("7. Sort students by GPA")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")
        
        if choice == '1':
            n = number_of_students()
            students = student_info(n)
        elif choice == '2':
            n = number_of_courses()
            courses = course_info(n)
        elif choice == '3':
            new_marks = input_marks(students, courses)
            if new_marks:
                marks_list.append(new_marks)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            student_marks(courses, students, marks_list)
        elif choice == '7':
            sort_students_by_gpa(students, courses, marks_list)
        elif choice == '8':
            print("Exiting. Please wait.")
            break
        else:
            print("Invalid option! Please choose between 1 and 8.")

# If this script is executed, main() will be executed
if __name__ == "__main__":
    main()