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
    print("\n== Withdraw Student ==")

    student_id = input("Enter Student ID: ").strip().upper()
    course_id = input("Enter Course ID: ").strip().upper()

    if student_id not in students:
        print("Student not found.")
        return

    if course_id not in courses:
        print("Course not found.")
        return

    if course_id not in students[student_id]["enrolments"]:
        print(f"{student_id} is not enrolled in {course_id}.")
        return

    confirm = input(
        f"Withdraw {student_id} from {course_id}? Their marks will be deleted. (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Withdrawal cancelled.")
        return

    courses[course_id]["roster"].remove(student_id)

    del students[student_id]["enrolments"][course_id]

    print(f"{student_id} withdrawn from {course_id}.")


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
    marks = students[student_id]["enrolments"][course_id]
    if len(marks) == 0:
        return None

    avg = sum(marks) / len(marks)
    return avg


# Reports

def student_transcript():
    print("\n== Student Transcript ==")

    student_id = input("Enter Student ID: ").strip().upper()

    if student_id not in students:
        print("Student not found.")
        return

    print(f"\nTRANSCRIPT - {student_id}: {students[student_id]['name']}")

    enrolments = students[student_id]["enrolments"]

    if len(enrolments) == 0:
        print("Student is not enrolled in any courses.")
        return

    total_marks = 0
    total_count = 0

    for course_id, marks in enrolments.items():

        course_name = courses[course_id]["name"]
        average = course_average_for(student_id, course_id)

        if average is None:
            status = "IN PROGRESS"
            average_display = "n/a"
        else:
            if average >= courses[course_id]["pass_mark"]:
                status = "PASS"
            else:
                status = "FAIL"

            average_display = round(average, 1)

            total_marks += sum(marks)
            total_count += len(marks)

        print(f"{course_id}: {course_name}")
        print(f"Marks: {len(marks)}")
        print(f"Average: {average_display}")
        print(f"Status: {status}\n")

    if total_count > 0:
        overall = total_marks / total_count
        print(f"Overall Average: {overall:.1f}")
    else:
        print("Overall Average: n/a")

def course_report():
    print("\n == Course Report == ")

    course_id = input("Enter Course ID: ").strip().upper()

    if course_id not in courses:
        print("Course not found.")
        return

    course = courses[course_id]

    print(f"\nCOURSE REPORT - {course_id}: {course['name']}")
    print(f"Pass Mark: {course['pass_mark']}")
    print(f"Enrolled: {len(course['roster'])} of {course['capacity']}")

    total_average = 0
    students_with_marks = 0

    print("\nStudents:")

    for student_id in course["roster"]:

        average = course_average_for(student_id, course_id)

        if average is None:
            print(f"{student_id} - {students[student_id]['name']} (No marks yet)")
        else:
            print(f"{student_id} - {students[student_id]['name']} : {average:.1f}")

            total_average += average
            students_with_marks += 1

    if students_with_marks > 0:
        course_average = total_average / students_with_marks
        print(f"\nCourse Average: {course_average:.1f}")
    else:
        print("\nCourse Average: n/a")

def search_everything():
    print("\n== Search ==")

    keyword = input("Enter search keyword: ").strip().lower()

    found = False

    print("\nStudents:")
    for student_id, student in students.items():
        if keyword in student["name"].lower():
            print(f"{student_id}: {student['name']}")
            found = True

    print("\nCourses:")
    for course_id, course in courses.items():
        if keyword in course["name"].lower():
            print(f"{course_id}: {course['name']}")
            found = True

    if not found:
        print("No matches.")


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



