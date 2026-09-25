#* num students
#* info: name, ID, Dob
#* num courses
#* Courses info: id, name
#* Select course and info 

#* list courses
#* list students
#* show student's mark for the given course

def number_of_students():
    return int(input("Enter number of students in the class: "))

def student_info(n):
    students = []
    for i in range(n):
        print(f"\nEnter info for student {i+1}:")
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
        print(f"\nEnter info for course {i+1}:")
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({"id": course_id, "name": name})
    return courses

def list_courses(courses):
    if not courses:
        print("No courses available.")
        return
    print("\n--- Course List ---")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    if not students:
        print("No students available.")
        return
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def input_marks(students, courses):
    if not students or not courses:
        print("Please enter both students and courses first.")
        return []
    
    list_courses(courses)
    course_id = input("Enter Course ID to input marks for: ")
    
    # Verify course exists
    selected_course = next((c for c in courses if c['id'] == course_id), None)
    if not selected_course:
        print("Course ID not found.")
        return []

    course_marks = {"course_id": course_id, "grades": {}}
    print(f"\nEntering marks for course: {selected_course['name']}")
    for student in students:
        mark = float(input(f"Mark for {student['name']} (ID: {student['id']}): "))
        course_marks["grades"][student['id']] = mark
        
    return course_marks

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
        
    print(f"\n--- Marks for Course ID: {course_id} ---")
    for student in students:
        score = target_marks["grades"].get(student['id'], "N/A")
        print(f"Student: {student['name']} (ID: {student['id']}) - Mark: {score}")

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
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
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
            print("Exiting. Please wait.")
            break
        else:
            print("Invalid option! Please choose between 1 and 7.")

if __name__ == "__main__":
    main()

