# Melsoft Campus Manager
# Python Essentials 1 Capstone Project

# Team Members:
# - Lisa Hlongwane
# - Ammaar Agjee
# - Kuhle Phungula

# Dictionaries
next_course_id = 1
next_student_id = 1
courses = {}
students = {}


# Menu

def show_menu():
    print("\n== Melsoft Campus Manager ==")
    print("1. Add Course")
    print("2. Register Student")
    print("3. Enrol Student in Course")
    print("4. Record a mark")
    print("5. Student Transcript")
    print("6. Course Report")
    print("7. Search")
    print("8. Withdraw Student from Course")
    print ("9. Academy report")
    print ("10. Exit")


# Validation

def read_valid_number(prompt, low, high):
 while True:
        try:
            number = int(input(prompt))
            if low <= number <= high:
                return number
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")   


# Courses

def add_course():
    global next_course_id
    
    print("\n== Add Course ==")
    course_id = "C" + str(next_course_id)
    course_name = input("Enter course name: ")
    max_students = read_valid_number("Enter maximum number of students: ", 1, 1000)
    courses[course_id] = {
        "name": course_name,
        "capacity": max_students,
        "roster": [],
    }

    next_course_id += 1

    print(f"Course '{course_id}' added successfully.")

     


# Students

def register_student():
    global next_student_id
    
    print("\n== Register Student ==")
    student_id = "S" + str(next_student_id)

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    
    if first_name == "" or last_name == "":
        print("Student name cannot be empty.")
        return

    if last_name == "":
        print("Student last name cannot be empty.")
        return
    
    students[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "enrolled_courses": {},
    }

    print(f"Student '{student_id}' registered successfully.")
    
    next_student_id += 1

# Enrolments

def enrol_student():
    pass


def withdraw_student():
    pass


# Marks

def record_mark():
    pass


def course_average_for(student_id, course_id):
    pass


# Reports

def student_transcript():
    pass


def course_report():
    pass


def search_everything():
    pass


def academy_totals():
    pass


def best_course():
    pass


def academy_report():
    pass


# Main Program

def main():
    while True:
        show_menu()
        choice = read_valid_number("Enter your choice (1-10): ", 1, 10)

        if choice == 1:
            add_course()
        elif choice == 2:
            register_student()
        elif choice == 3:
            enrol_student()
        elif choice == 4:
            record_mark()
        elif choice == 5:
            student_transcript()
        elif choice == 6:
            course_report()
        elif choice == 7:
            search_everything()
        elif choice == 8:
            withdraw_student()
        elif choice == 9:
            academy_report()
        elif choice == 10:
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
