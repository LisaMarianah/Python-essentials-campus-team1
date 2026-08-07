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
    print(f"Course '{course_id}' added successfully.")

     


# Students



# Enrols a student to a course, with multiple checks before confirming enrolment

def enrol_student(students, courses):
    student_id = input("Enter student ID: ").strip().upper()
    if student_id not in students:
        print("Student not found.")
        return students, courses

    course_id = input("Enter course ID: ").strip().upper()
    if course_id not in courses:
        print("Course not found.")
        return students, courses

    if len(courses[course_id]["roster"]) >= 2:
        print(course_id, "is full (2 of 2 enrolled).")
        return students, courses

    if student_id in courses[course_id]["roster"]:
        print(student_id, "is already enrolled in", course_id, ".")
        return students, courses

    courses[course_id]["roster"].append(student_id)
    students[student_id]["enrolments"][course_id] = []
    print(student_id, "enrolled in", course_id, ":", courses[course_id]["name"], ".")
    return students, courses 




def withdraw_student():
    pass


# Marks

def record_mark(students, courses):
    student_id = input("Enter student ID: ").strip().upper()
    if student_id not in students:
        print("Student not found.")
        return students, courses

    course_id = input("Enter course ID: ").strip().upper()
    if course_id not in courses:
        print("Course not found.")
        return students, courses

    if student_id not in courses[course_id]["roster"]:
        print(student_id, "is not enrolled in", course_id, ".")
        return students, courses

    mark = input("Enter a mark: ").strip()
    if mark == "":
        print("Mark cannot be blank.")
        return students, courses
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            print("Invalid mark. Mark must be between 0 and 100.")
            return None
        else:
            return mark
    except ValueError:
        print("Invalid mark.")
        return None

    students[student_id]["enrolments"].append(mark)
    print("Mark:", mark, "recorded for", student_id, "in", course_id, ".")
    return students, courses 


    


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
            record_mark(students, courses)
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



