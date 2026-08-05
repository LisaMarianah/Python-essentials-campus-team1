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
    


# Validation

def read_valid_number(prompt, low, high):
    pass


# Courses

def add_course():
    pass


# Registers a new student with an empty enrolments dictionary, and loops until valid name is given

def register_student(students):
    global next_student_number
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be blank. Please try again.")
        else:
            break
    student_id = "S" + str(next_student_number)
    next_student_number += 1
    students[student_id] = {"name": name, "enrolled_courses": {}}
    print("Registered", student_id, ":", name)
    return students 


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
    pass

if __name__ == "__main__":
    main()
