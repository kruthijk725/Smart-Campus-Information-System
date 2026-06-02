import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.marks = []


    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def add_marks(self, mark):
        self.marks.append(mark)


    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)


    def evaluate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'


    def to_dict(self):
        return {
            'Student ID': self.student_id,
            'Name': self.name,
            'Age': self.age,
            'Courses': self.courses,
            'Marks': self.marks,
            'Average': self.calculate_average(),
            'Grade': self.evaluate_grade()
        }



def calculate_fee(number_of_courses):
    base_fee = 5000
    course_fee = 2000

    total_fee = base_fee + (number_of_courses * course_fee)
    return total_fee



def save_records(student_list, filename='students.json'):
    data = [student.to_dict() for student in student_list]

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print("Student records saved successfully.\n")



def load_records(filename='students.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print("No student record file found.\n")
        return []



def search_student(student_list, search_id):
    for student in student_list:
        if student.student_id == search_id:
            return student

    return None


def sort_students(student_list):
    return sorted(student_list,
                  key=lambda student: student.calculate_average(),
                  reverse=True)


def scan_directory(path):
    try:
        print(f"\nScanning directory: {path}\n")

        files = os.listdir(path)

        if len(files) == 0:
            print("Directory is empty.\n")
        else:
            for file in files:
                print(file)

    except FileNotFoundError:
        print("Directory not found.\n")

    except PermissionError:
        print("Permission denied while accessing directory.\n")

    except Exception as error:
        print("An unexpected error occurred:", error)



def performance_analytics(student_list):

    data = {
        'Name': [],
        'Average Marks': []
    }

    for student in student_list:
        data['Name'].append(student.name)
        data['Average Marks'].append(student.calculate_average())

    # Pandas DataFrame
    df = pd.DataFrame(data)

    print("\nStudent Performance Data\n")
    print(df)

    # NumPy operations
    marks_array = np.array(data['Average Marks'])

    print("\nAnalytics Report")
    print("Highest Average:", np.max(marks_array))
    print("Lowest Average:", np.min(marks_array))
    print("Overall Mean:", np.mean(marks_array))

    # Matplotlib visualization
    plt.figure(figsize=(8, 5))
    plt.bar(df['Name'], df['Average Marks'])
    plt.xlabel('Student Name')
    plt.ylabel('Average Marks')
    plt.title('Student Performance Analysis')
    plt.show()


def main():

    students = []

    while True:

        print("\n===== SMART CAMPUS INFORMATION SYSTEM =====")
        print("1. Register Student")
        print("2. Enroll Course")
        print("3. Add Marks")
        print("4. Display Student Records")
        print("5. Search Student")
        print("6. Sort Students by Performance")
        print("7. Calculate Fee")
        print("8. Save Records to File")
        print("9. Load Records from File")
        print("10. Scan Directory")
        print("11. Student Analytics")
        print("12. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            student = Student(sid, name, age)
            students.append(student)

            print("Student registered successfully.\n")

        elif choice == '2':
            sid = input("Enter Student ID: ")
            student = search_student(students, sid)

            if student:
                course = input("Enter Course Name: ")
                student.enroll_course(course)
                print("Course enrolled successfully.\n")
            else:
                print("Student not found.\n")


        elif choice == '3':
            sid = input("Enter Student ID: ")
            student = search_student(students, sid)

            if student:
                mark = float(input("Enter Marks: "))
                student.add_marks(mark)
                print("Marks added successfully.\n")
            else:
                print("Student not found.\n")

        elif choice == '4':
            print("\nSTUDENT RECORDS\n")

            for student in students:
                print(student.to_dict())


        elif choice == '5':
            sid = input("Enter Student ID to search: ")
            student = search_student(students, sid)

            if student:
                print(student.to_dict())
            else:
                print("Student not found.\n")

        elif choice == '6':
            sorted_students = sort_students(students)

            print("\nStudents Sorted by Performance\n")

            for student in sorted_students:
                print(student.name,
                      "- Average:",
                      student.calculate_average())


        elif choice == '7':
            sid = input("Enter Student ID: ")
            student = search_student(students, sid)

            if student:
                total_fee = calculate_fee(len(student.courses))
                print("Total Fee =", total_fee)
            else:
                print("Student not found.\n")


        elif choice == '8':
            save_records(students)

        elif choice == '9':
            data = load_records()

            print("\nLoaded Student Records\n")

            for record in data:
                print(record)


        elif choice == '10':
            path = input("Enter directory path: ")
            scan_directory(path)


        elif choice == '11':
            if len(students) > 0:
                performance_analytics(students)
            else:
                print("No student data available.\n")



        elif choice == '12':
            print("Exiting Smart Campus Information System...")
            break

        else:
            print("Invalid choice. Please try again.\n")



main()