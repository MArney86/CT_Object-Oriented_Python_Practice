import re

#Begin part 1
    #Define Student class with attributes and methods as defined in assignment
class Student:
    name: str = ""
    email: str = ""
    grades: list[int] = []

    def __init__(self, name: str, email: str, grades: list[int]) -> None:
        self.name = name
        self.email = email
        self.grades = grades
    
    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

#Begin part 4 
    #add method to return grades as tuple        
    def grades_tuple(self) -> tuple[int, ...]:
        return tuple(self.grades)
#part 4 continued in main()
#End part 1

#Begin part 2
    #create 3 initialzed instances of Students
studentA = Student("Alice Smith", "alice.smith@example.com", [85, 90, 78])
studentB = Student("Bob Johnson", "bjohnson@fakeemails.net", [92, 88, 95, 100])
studentC = Student("Charlie Brown", "charlie.B@fauxaddress.co.jp", [70, 75, 80, 65])
#Part 2 continued in main()
#Begin part 6
    # use regular expressions to validate email format
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
#Part 6 continued in main()
#Begin part 3
    #create dictionary of students with email as key
student_dict = {
    studentA.email: studentA,
    studentB.email: studentB,
    studentC.email: studentC
}

def find_student_by_email(email: str) -> Student | None:
    return student_dict.get(email, None)
#part 3 continued in main()


def main() -> None:
    
    #Part2 continued: add grades and display info and average grades for each Student
    studentA.add_grade(88)
    studentA.add_grade(72)
    studentB.add_grade(89)
    studentB.add_grade(94)
    studentC.add_grade(90)
    studentC.add_grade(85)

    
    studentA.display_info()
    print(f"Average Grade: {studentA.average_grade():.2f}\n")
    studentB.display_info()
    print(f"Average Grade: {studentB.average_grade():.2f}\n")
    studentC.display_info()
    print(f"Average Grade: {studentC.average_grade():.2f}\n")
    #End part 2
    #Part 3 continued: search for students by email and display their info
    emails_to_search = ["alice.smith@example.com", "bjohnson@fakeemails.net", "charlie.B@fauxaddress.co.jp"]
    for email in emails_to_search:
        student: Student | None = find_student_by_email(email)
        if student:
            print(f"Student found for email {email}:")
            print(f"Name: {student.name}\n")
        else:
            print(f"No student found with email: {email}\n")

    unique_grades: set[int] = set()
    for student in student_dict.values():
        unique_grades.update(student.grades)
    print(f"Unique grades across all students: {sorted(unique_grades)}\n")
    #End part 3
    #Part 4 continued: display grades as tuple for each student and demonstrate immutability
    for student in student_dict.values():
        grades_tuple: tuple[int, ...] = student.grades_tuple()
        print(f"{student.name}'s grades (as tuple): {grades_tuple}")
        try:
            print(f"Attempting to modify grades tuple for {student.name}...")
            grades_tuple[0] = 100  # type: ignore  # Attempt to modify the tuple
        except TypeError as e:
            print(f"Cannot modify grades tuple for {student.name}: {e}\n")
    #End part 4

    #begin part 5
        #Remove the last grade from each student's grades list
    for student in student_dict.values():
        if student.grades:
            removed_grade: int = student.grades.pop()
            print(f"Removed grade {removed_grade} from {student.name}'s grades.")
            print(f"First and last grades are now: {student.grades[0]}, {student.grades[-1]} with a total of {len(student.grades)} grades.\n")
    #end part 5

    #part 6 continued: validate emails then print count of all grades above 90 for all students
    test_emails: list[str] = list(student_dict.keys())
    for email in test_emails:
        student: Student | None = find_student_by_email(email)
        if is_valid_email(email):
            if student and student.name:
                print(f"Email '{email} from {student.name}' is valid.\n")
            else:
                print(f"Email '{email}' is valid but not attributed to a student.\n")
        else:
            print(f"Email '{email}' is invalid.\n")
    high_grades: int = 0
    for student in student_dict.values():
        for grade in student.grades:
            if grade > 90:
                high_grades += 1
    
    print(f"Total number of grades above 90 across all students: {high_grades}")

if __name__ == "__main__":
    main()