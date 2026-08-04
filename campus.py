# Melsoft Campus Manager
# Python Essentials 1 Capstone Project

# Team Members:
# - Lisa Hlongwane
# - Ammaar Agjee
# - Kuhle Phungula

# Dictionaries
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
    pass


# Students


def register_student():
    pass


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
