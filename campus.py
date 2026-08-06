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
    pass


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
    pass

if __name__ == "__main__":
    main()
