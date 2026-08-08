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
    
    capacity = courses[course_id]["capacity"]
    if len(courses[course_id]["roster"]) >= capacity:
        print(course_id, "is full (" + str(capacity) + "of" + str(capacity) + "enrolled).")
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


# Records a mark for a student in a specific course, and mark validated in a try-except

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
    except ValueError:
        print("Invalid mark.")
        return students, courses

    if mark < 0 or mark > 100:
        print("Invalid mark. Mark must be between 0 and 100.")
        return students, courses 

    students[student_id]["enrolments"][course_id].append(mark)
    print("Mark:", mark, "recorded for", student_id, "in", course_id, ".")
    return students, courses 


    


def course_average_for(student_id, course_id):
    marks = students[student_id]["enrolments"][course_id]
    if len(marks) == 0:
        return None

    avg = sum(marks) / len(marks)
    return avg


# Reports

def student_transcript():
    pass


def course_report():
    pass


def search_everything():
    pass

# Finds the total students, enrolments, and marks
def academy_totals(students):
    total_students = len(students)

    total_enrolments = 0
    total_marks = 0

    for student_id in students:
        for marks in students[student_id]["enrolments"].values():
            total_enrolments += 1
            total_marks += len(marks)

    return (total_students, total_enrolments, total_marks)

# Finds course and its averages
def best_course(courses, students):
    if not courses:
        return (None, None)

    best_id = None
    best_average = None

    for course_id in courses:
        total_average = 0
        students_with_marks = 0

        for student_id in courses[course_id]["roster"]:
            average = course_average_for(student_id, course_id)
            if average is None:
                total_average += average
                students_with_marks += 1

        if students_with_marks == 0:
            continue

        course_average = total_average / students_with_marks

        if best_average is None or course_average > best_average:
            best_average = course_average
            best_id = course_id

    if best_id is None:
        return (None, None)

    return (best_id, best_average)


def academy_report():
    print("\n === Academy Report ===")

    total_students, total_enrolments, total_marks = academy_totals(students)
    total_courses = len(courses)

    print("Total Students: ", total_students)
    print("Total Courses: ", total_courses)
    print("Total Enrolments: ", total_enrolments)
    print("Marks Recorded: ", total_marks)

    marks_sum = 0
    distinction = []
    at_risk = []

    for student_id in students:
        students_marks = []
        for marks in students[student_id]["enrolments"].values():
            students_marks.extend(marks)

        marks_sum += sum(students_marks)

        if len(students_marks) == 0:
            continue

        overall_average = sum(students_marks) / len(students_marks)
        if overall_average >= 80:
            distinction.append(student_id, ":", students[student_id]["name"])
        elif overall_average < 50:
            at_risk.append(student_id, ":", students[student_id]["name"])

    if total_marks > 0:
        academy_average = marks_sum / total_marks
        print("Academy-wide Average: ", academy_average)
    else:
        print("Academy-wide Average: n/a")

    best_id, best_average = best_course(courses, students)
    if best_id is None:
        print("Best-performing Course: n/a (no marks recorded yet)")
    else:
        print("Best-performing Course: ", best_id, "-", courses[best_id]["name"], "-", best_average)

    print("Distinction list (avg 80+): ", distinction)
    print("At risk list (avg below 50): ", at_risk)



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



