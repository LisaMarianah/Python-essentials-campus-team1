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

    # Make sure the course name isn't blank
    while True:
        course_name = input("Enter course name: ").strip()
        if course_name == "":
            print("Course name cannot be blank.")
        else:
            break

    max_students = read_valid_number(
        "Enter maximum number of students: ", 1, 1000
    )

    pass_mark = read_valid_number(
        "Enter pass mark (0-100): ", 0, 100
    )

    courses[course_id] = {
        "name": course_name,
        "capacity": max_students,
        "pass_mark": pass_mark,
        "roster": []
    }

    print(f"Added {course_id}: {course_name} (capacity {max_students}, pass mark {pass_mark})")
    next_course_id += 1

# Registers a new student with an empty enrolments dictionary, and loops until valid name is given

def register_student():
    global next_student_id

    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be blank. Please try again.")
        else:
            break

    student_id = "S" + str(next_student_id)
    next_student_id += 1

    students[student_id] = {
        "name": name,
        "enrolments": {}
    }

    print(f"Registered {student_id}: {name}")


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

next_student_number = 1
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
