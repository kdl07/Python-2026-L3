import curses
from input import number_of_students, student_info, number_of_courses, course_info, input_marks
from output import list_courses, list_students, student_marks, sort_students_by_gpa

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