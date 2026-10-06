import os
from input import number_of_students, student_info, number_of_courses, course_info, input_marks
from output import list_courses, list_students, student_marks, sort_students_by_gpa
from storage import load_data, save_data

def main():
    # Load data on startup using compressed pickle
    students, courses, marks_list = load_data()

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
            new_marks = input_marks(students, courses, marks_list)
        elif choice == '4':
            list_courses(courses)
        elif choice == '5':
            list_students(students)
        elif choice == '6':
            student_marks(courses, students, marks_list)
        elif choice == '7':
            sort_students_by_gpa(students, courses, marks_list)
        elif choice == '8':
            # Save data compressed on exit
            save_data(students, courses, marks_list)
            print("Data saved and compressed successfully. Exiting...")
            break
        else:
            print("Invalid option! Please choose between 1 and 8.")

if __name__ == "__main__":
    main()