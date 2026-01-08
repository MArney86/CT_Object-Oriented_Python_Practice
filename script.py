import re

# ============================================================================
# PART 1: CLASS DEFINITION
# ============================================================================
# Define Student class with attributes and methods as defined in assignment

class Student:
    name: str = ""
    email: str = ""
    grades: list[int] = []

    def __init__(self, name: str, email: str, grades: list[int]) -> None:
        """Initialize a Student with name, email, and grades."""
        self.name = name
        self.email = email
        self.grades = grades
    
    def add_grade(self, grade: int) -> None:
        """Add a single grade to the student's grades list."""
        self.grades.append(grade)

    def average_grade(self) -> float:
        """Calculate and return the average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self) -> None:
        """Print the student's name and email information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

    # Part 4: Add method to return grades as tuple (continued in main())        
    def grades_tuple(self) -> tuple[int, ...]:
        """Return the student's grades as an immutable tuple."""
        return tuple(self.grades)


# ============================================================================
# PART 2: WORKING WITH OBJECTS
# ============================================================================
# Create 3 initialized instances of Student objects
studentA = Student("Alice Smith", "alice.smith@example.com", [85, 90, 78])
studentB = Student("Bob Johnson", "bjohnson@fakeemails.net", [92, 88, 95, 100])
studentC = Student("Charlie Brown", "charlie.B@fauxaddress.co.jp", [70, 75, 80, 65])


# ============================================================================
# PART 6 (BONUS): EMAIL VALIDATION
# ============================================================================
# Use regular expressions to validate email format

def is_valid_email(email: str) -> bool:
    """Validate email format using regex pattern (name@domain.com)."""
    """Validate email format using regex pattern (name@domain.com)."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# ============================================================================
# PART 3: DICTIONARY & SET INTEGRATION
# ============================================================================
# Create dictionary of students with email as key
student_dict = {
    studentA.email: studentA,
    studentB.email: studentB,
    studentC.email: studentC
}

def find_student_by_email(email: str) -> Student | None:
    """Safely retrieve a Student object by email using .get() method."""
    return student_dict.get(email, None)


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main() -> None:
    """Main function demonstrating all parts of the assignment."""
    """Main function demonstrating all parts of the assignment."""
    
    # ========================================================================
    # PART 2 CONTINUED: Add grades and display student information
    # ========================================================================
    studentA.add_grade(88)
    studentA.add_grade(72)
    studentB.add_grade(89)
    studentB.add_grade(94)
    studentC.add_grade(90)
    studentC.add_grade(85)

    # Display information and average grades for each student
    studentA.display_info()
    print(f"Average Grade: {studentA.average_grade():.2f}\n")
    studentB.display_info()
    print(f"Average Grade: {studentB.average_grade():.2f}\n")
    studentC.display_info()
    print(f"Average Grade: {studentC.average_grade():.2f}\n")
    
    # ========================================================================
    # PART 3 CONTINUED: Dictionary operations and set creation
    # ========================================================================
    # Search for students by email and display their information
    emails_to_search = ["alice.smith@example.com", "bjohnson@fakeemails.net", "charlie.B@fauxaddress.co.jp"]
    for email in emails_to_search:
        student: Student | None = find_student_by_email(email)
        if student:
            print(f"Student found for email {email}:")
            print(f"Name: {student.name}\n")
        else:
            print(f"No student found with email: {email}\n")

    # Create a set of unique grades across all students
    unique_grades: set[int] = set()
    for student in student_dict.values():
        unique_grades.update(student.grades)
    print(f"Unique grades across all students: {sorted(unique_grades)}\n")
    
    # ========================================================================
    # PART 4 CONTINUED: Tuple practice and immutability demonstration
    # ========================================================================
    for student in student_dict.values():
        grades_tuple: tuple[int, ...] = student.grades_tuple()
        print(f"{student.name}'s grades (as tuple): {grades_tuple}")
        try:
            print(f"Attempting to modify grades tuple for {student.name}...")
            grades_tuple[0] = 100  # type: ignore - intentionally causes error
        except TypeError as e:
            print(f"Cannot modify grades tuple for {student.name}: {e}\n")
    
    # ========================================================================
    # PART 5: LIST OPERATIONS
    # ========================================================================
    # Remove the last grade from each student's grades list using .pop()
    for student in student_dict.values():
        if student.grades:
            removed_grade: int = student.grades.pop()
            print(f"Removed grade {removed_grade} from {student.name}'s grades.")
            print(f"First and last grades are now: {student.grades[0]}, {student.grades[-1]} with a total of {len(student.grades)} grades.\n")
    
    # ========================================================================
    # PART 6 CONTINUED: Email validation and grade counting
    # ========================================================================
    # Validate all student emails using regular expressions
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
    
    # Count how many grades are above 90 across all students
    high_grades: int = 0
    for student in student_dict.values():
        for grade in student.grades:
            if grade > 90:
                high_grades += 1
    
    print(f"Total number of grades above 90 across all students: {high_grades}")

if __name__ == "__main__":
    main()