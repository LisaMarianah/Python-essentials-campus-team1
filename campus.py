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


# Students


def register_student():
    pass


# Enrolments

def enrol_student():
    pass


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

def record_mark():
    pass


def course_average_for(student_id, course_id):
    pass


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

def main():
    pass

if __name__ == "__main__":
    main()
