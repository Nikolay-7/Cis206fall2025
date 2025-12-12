# ------------------------------------------------------------
# CIS 206 – Assignment 16-Project  
# Modules, Classes & Class Diagram Project
#
# Team Members:
# - Wang Ko Cheung
# - Amtoj Singh
# - Afshin Kerka
# - Nikolay Neykov
# ------------------------------------------------------------

import json


# -------------------- 1) Base Class: Person --------------------

class Person:
#Represents a general person in the academic system.
    def __init__(self, personID, firstName, lastName, email, dateOfBirth):
        self.personID = personID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.dateOfBirth = dateOfBirth

    def to_dict(self):
#Converts to dictionary for JSON export.
        return {
            'personID': self.personID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'dateOfBirth': self.dateOfBirth
        }


# -------------------- 2) Single Inheritance: Student --------------------

class Student(Person):
#Represents a student in the system.
    def __init__(self, personID, firstName, lastName, email, dateOfBirth,
                 major, gpa, expectedGraduationDate):
        super().__init__(personID, firstName, lastName, email, dateOfBirth)
        self.major = major
        self.gpa = gpa
        self.expectedGraduationDate = expectedGraduationDate
        self.enrollments = []

    def to_dict(self):
#Converts to dictionary for JSON export.
        data = super().to_dict()
        data.update({
            'type': 'Student',
            'major': self.major,
            'gpa': self.gpa,
            'expectedGraduationDate': self.expectedGraduationDate
        })
        return data


# -------------------- 3) Single Inheritance: Instructor --------------------

class Instructor(Person):
#Represents an instructor.
    def __init__(self, personID, firstName, lastName, email, dateOfBirth,
                 rank, officeHours):
        super().__init__(personID, firstName, lastName, email, dateOfBirth)
        self.rank = rank
        self.officeHours = officeHours

    def to_dict(self):
#Converts to dictionary for JSON export.
        data = super().to_dict()
        data.update({
            'type': 'Instructor',
            'rank': self.rank,
            'officeHours': self.officeHours
        })
        return data


# -------------------- 4) Multiple Inheritance: TeachingAssistant --------------------

class TeachingAssistant(Student, Instructor):
#Represents a teaching assistant who is both a student and an instructor.
    def __init__(self, personID, firstName, lastName, email, dateOfBirth,
                 major, gpa, expectedGraduationDate,
                 rank, officeHours,
                 assistantshipStipend, hoursPerWeek):

#Calls Person initializer manually (to avoid multiple inheritance conflict).
        Person.__init__(self, personID, firstName, lastName, email, dateOfBirth)

#Student attributes.
        self.major = major
        self.gpa = gpa
        self.expectedGraduationDate = expectedGraduationDate
        self.enrollments = []

#Instructor attributes.
        self.rank = rank
        self.officeHours = officeHours

#TA-specific attributes.
        self.assistantshipStipend = assistantshipStipend
        self.hoursPerWeek = hoursPerWeek

    def to_dict(self):
#Converts to dictionary for JSON export.
        data = Person.to_dict(self)
        data.update({
            'type': 'TeachingAssistant',
            'major': self.major,
            'gpa': self.gpa,
            'expectedGraduationDate': self.expectedGraduationDate,
            'rank': self.rank,
            'officeHours': self.officeHours,
            'assistantshipStipend': self.assistantshipStipend,
            'hoursPerWeek': self.hoursPerWeek
        })
        return data


# -------------------- 5) Course --------------------

class Course:
#Represents a course.
    def __init__(self, courseID, title, description, credits):
        self.courseID = courseID
        self.title = title
        self.description = description
        self.credits = credits
        self.sections = []

    def to_dict(self):
#Converts to dictionary for JSON export.
        return {
            'courseID': self.courseID,
            'title': self.title,
            'description': self.description,
            'credits': self.credits
        }


# -------------------- 6) Section --------------------

class Section:
#Represents one section of a course in a given semester.
    def __init__(self, sectionID, semester, year, location, meetingTime, course, instructor):
        self.sectionID = sectionID
        self.semester = semester
        self.year = year
        self.location = location
        self.meetingTime = meetingTime
        self.course = course
        self.instructor = instructor
        self.enrollments = []

    def to_dict(self):
#Converts to dictionary for JSON export.
        return {
            'sectionID': self.sectionID,
            'semester': self.semester,
            'year': self.year,
            'location': self.location,
            'meetingTime': self.meetingTime,
            'courseID': self.course.courseID,
            'instructorID': self.instructor.personID
        }


# -------------------- 7) Enrollment --------------------

class Enrollment:
#Represents a student enrolled in a specific course section.
    def __init__(self, enrollmentID, enrollmentDate, student, section):
        self.enrollmentID = enrollmentID
        self.enrollmentDate = enrollmentDate
        self.student = student
        self.section = section
        self.grade: str | None = None

#Updates references.
        student.enrollments.append(self)
        section.enrollments.append(self)

    def to_dict(self):
#Converts to dictionary for JSON export.
        return {
            'enrollmentID': self.enrollmentID,
            'enrollmentDate': self.enrollmentDate,
            'studentID': self.student.personID,
            'sectionID': self.section.sectionID,
            'grade': self.grade
        }


# -------------------- 8) JSON Export Functions --------------------

def export_to_json(courses, people, sections, enrollments, filename='academic_data.json'):
#Exports all academic data to a JSON file.
    data = {
        'courses': [course.to_dict() for course in courses],
        'people': [person.to_dict() for person in people],
        'sections': [section.to_dict() for section in sections],
        'enrollments': [enrollment.to_dict() for enrollment in enrollments]
    }


def view_json_file(filename='academic_data.json'):
#Displays the contents of the JSON file in a readable format.
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        print(f"\n---------- JSON File Content Preview ----------")
        print(f"\nTotal Records:")
        print(f"  - Courses: {len(data.get('courses', []))}")
        print(f"  - People: {len(data.get('people', []))}")
        print(f"  - Sections: {len(data.get('sections', []))}")
        print(f"  - Enrollments: {len(data.get('enrollments', []))}")

#Shows sample data.
        if data.get('people'):
            print(f"\nSample Person Record:")
            print(json.dumps(data['people'][0], indent=2))

        if data.get('enrollments'):
            print(f"\nSample Enrollment Record:")
            print(json.dumps(data['enrollments'][0], indent=2))

    except FileNotFoundError:
        print(f"\n File '{filename}' not found")
    except json.JSONDecodeError:
        print(f"\n Error reading JSON from '{filename}'")


# -------------------- Test the Classes --------------------

if __name__ == "__main__":
    print("------------ Academic System Test Output ------------\n")

#Creates a Course.
    CIS106 = Course("CIS 106", "Computer Logic and Programming Technology",
                    "Introduction to programming concepts", 3)
    print(f"Created Course: {CIS106.title} ({CIS106.courseID}), {CIS106.credits} credits")

#Creates an Instructor.
    prof_sanders = Instructor("I01", "Albert", "Sanders", "asanders@university.edu",
                              "1971-04-16", "Professor", "Mon/Wed 1-3 PM")
    print(f"Created Instructor: {prof_sanders.firstName} {prof_sanders.lastName} ({prof_sanders.rank})")

#Creates a Section.
    CIS106_fall = Section("SEC01", "Fall", 2025, "Room 108", "MWF 10-11 AM", CIS106, prof_sanders)
    CIS106.sections.append(CIS106_fall)
    print(f"Created Section: {CIS106_fall.sectionID} - {CIS106_fall.semester} {CIS106_fall.year}")

#Creates Students.
    alex = Student("S01", "Alex", "Robinson", "arobinson@student.edu",
                   "2004-08-20", "CIS", 3.5, "2025-05-15")

    adam = Student("S02", "Adam", "Simpson", "asimpson@student.edu",
                   "2004-11-12", "CIS", 3.3, "2025-05-15")

    print("\nCreated Students:")
    print(f" - {alex.firstName} {alex.lastName}, Major: {alex.major}, GPA: {alex.gpa}")
    print(f" - {adam.firstName} {adam.lastName}, Major: {adam.major}, GPA: {adam.gpa}")

#Enrolls Students.
    enrollment1 = Enrollment("E01", "2024-08-25", alex, CIS106_fall)
    enrollment2 = Enrollment("E02", "2024-08-26", adam, CIS106_fall)
    enrollment1.grade = "A"
    enrollment2.grade = "B"

    print("\nEnrollments:")
    print(f" - {alex.firstName} enrolled with grade {enrollment1.grade}")
    print(f" - {adam.firstName} enrolled with grade {enrollment2.grade}")

#Creates Teaching Assistant.
    eric = TeachingAssistant("TA01", "Eric", "Benson", "ebenson@university.edu",
                             "2001-03-10", "CIS", 3.9, "2024-12-15",
                             "Graduate TA", "Thu 4-8 PM",
                             2000, 20)

    print("\nCreated Teaching Assistant:")
    print(f" - {eric.firstName} {eric.lastName}, GPA: {eric.gpa}")
    print(f" - TA Stipend: ${eric.assistantshipStipend}/month, Hours: {eric.hoursPerWeek}/week")
    print(f" - Office Hours: {eric.officeHours}")

    print("\nEnrollment Summary:")
    print(f"Total students enrolled in {CIS106.title}: {len(CIS106_fall.enrollments)}")

    # -------------------- JSON Export Process --------------------
    print("\n" + "*"*40)
    print("JSON Export To Store All Academic Data")
    print("*"*40)

#Collects all objects for export.
    all_courses = [CIS106]
    all_people = [prof_sanders, alex, adam, eric]
    all_sections = [CIS106_fall]
    all_enrollments = [enrollment1, enrollment2]

#Exports to JSON.
    export_to_json(all_courses, all_people, all_sections, all_enrollments)

#View the exported JSON file
    view_json_file()

    print("\n" + "*"*70)
    print("Please Check 'academic_data.json' File For Complete Academic Data")
    print("*"*70)