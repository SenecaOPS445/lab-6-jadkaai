#!/usr/bin/env python3
# Author ID: jkaai

class Student:

    # Define the name and number when a student object is created, ex. student1 = Student('john', 25969102)
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert the number to a string to avoid TypeError
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and return a string
    def displayGPA(self):
        if len(self.courses) == 0:
            gpa = 0.0
        else:
            gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    # Return a list of course that the student passed (not a 0.0 grade)
    def displayCourses(self):
        passed_courses = [course for course in self.courses if self.courses[course] > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
