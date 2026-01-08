# Object-Oriented Python Practice: Student Management System

A comprehensive Python project demonstrating object-oriented programming (OOP) principles, data structures, and Python best practices through a student grade management system.

## 📋 Project Overview

This project implements a `Student` class to manage student information and grades, showcasing key Python concepts including:
- **Object-Oriented Programming**: Classes, objects, methods, and attributes
- **Data Structures**: Lists, tuples, sets, and dictionaries
- **Data Validation**: Email validation using regular expressions
- **Error Handling**: Exception handling with try/except blocks
- **Type Hints**: Modern Python type annotations for better code clarity

## 🎯 Learning Objectives

This project fulfills the following requirements:

### Part 1: Class Definition ✓
- Created `Student` class with `name`, `email`, and `grades` attributes
- Implemented `add_grade()` method to add grades to the list
- Implemented `average_grade()` method to calculate grade averages
- Implemented `display_info()` method to print student information

### Part 2: Working with Objects ✓
- Created 3 student objects with different attributes
- Added 2 new grades to each student
- Displayed information and average grades for each student

### Part 3: Dictionary & Set Integration ✓
- Created `student_dict` mapping emails to Student objects
- Implemented `find_student_by_email()` function with safe `.get()` retrieval
- Generated a set of unique grades across all students

### Part 4: Tuple Practice ✓
- Added `grades_tuple()` method to return grades as a tuple
- Demonstrated tuple immutability with try/except error handling

### Part 5: List Operations ✓
- Removed last grade from each student using `.pop()`
- Accessed and printed first and last grades
- Used `len()` to count grades for each student

### Part 6: Bonus Features ✓
- Validated email formats using regular expressions
- Counted grades above 90 across all students

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher (uses modern type hints with `|` union syntax)
- No external dependencies required (uses only standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CT_Object-Oriented_Python_Practice.git
cd CT_Object-Oriented_Python_Practice
```

2. Run the script:
```bash
python script.py
```

## 📂 Project Structure

```
CT_Object-Oriented_Python_Practice/
│
├── README.md          # Project documentation
└── script.py          # Main Python script with Student class and demonstrations
```

## 💻 Code Features

### Student Class

```python
class Student:
    """Manages student information and grades"""
    
    def __init__(self, name: str, email: str, grades: list[int])
    def add_grade(self, grade: int) -> None
    def average_grade(self) -> float
    def display_info(self) -> None
    def grades_tuple(self) -> tuple[int, ...]
```

### Key Functions

- `is_valid_email(email: str) -> bool`: Validates email format using regex
- `find_student_by_email(email: str) -> Student | None`: Safely retrieves students from dictionary

## 📊 Sample Output

```
Name: Alice Smith
Email: alice.smith@example.com
Average Grade: 82.60

Student found for email alice.smith@example.com:
Name: Alice Smith

Unique grades across all students: [65, 70, 72, 75, 78, 80, 85, 88, 89, 90, 92, 94, 95, 100]

Alice Smith's grades (as tuple): (85, 90, 78, 88, 72)
Attempting to modify grades tuple for Alice Smith...
Cannot modify grades tuple for Alice Smith: 'tuple' object does not support item assignment

Removed grade 72 from Alice Smith's grades.
First and last grades are now: 85, 88 with a total of 4 grades.

Total number of grades above 90 across all students: 5
```

## 🔍 Key Concepts Demonstrated

### 1. **Object-Oriented Programming**
- Encapsulation of student data and behaviors in a class
- Instance methods operating on object state
- Constructor (`__init__`) for object initialization

### 2. **Data Structures**
- **Lists**: Mutable sequences for storing grades
- **Tuples**: Immutable sequences demonstrating data protection
- **Sets**: Automatic deduplication of grades
- **Dictionaries**: Key-value mapping for fast student lookup

### 3. **Type Safety**
- Modern Python type hints for all functions and methods
- Union types using `|` operator (Python 3.10+)
- Return type annotations for clarity

### 4. **Error Handling**
- Try/except blocks for catching tuple modification errors
- Safe dictionary access with `.get()`
- Validation checks before operations

### 5. **Regular Expressions**
- Email validation pattern matching
- Format: `name@domain.com`

## 🎓 Educational Value

This project demonstrates:
- **Clean Code**: Well-commented, readable, and maintainable
- **Best Practices**: Type hints, docstrings, and proper naming conventions
- **Practical Application**: Real-world student management scenario
- **Comprehensive Coverage**: Multiple Python concepts in one cohesive project

## 📝 Assignment Rubric Compliance

| Requirement | Status | Implementation |
|------------|--------|----------------|
| Class with attributes | ✅ | Student class with name, email, grades |
| add_grade method | ✅ | Appends grades to list |
| average_grade method | ✅ | Calculates mean with zero-division handling |
| display_info method | ✅ | Prints formatted student information |
| 3 student objects | ✅ | Alice, Bob, and Charlie created |
| Add 2 grades per student | ✅ | All students receive 2 additional grades |
| Dictionary mapping | ✅ | student_dict maps email → Student |
| Safe retrieval function | ✅ | find_student_by_email with .get() |
| Unique grades set | ✅ | Set created and printed |
| grades_tuple method | ✅ | Returns grades as immutable tuple |
| Tuple immutability demo | ✅ | Try/except catches TypeError |
| List .pop() operation | ✅ | Removes last grade from each student |
| First/last access | ✅ | Uses indexing [0] and [-1] |
| len() usage | ✅ | Counts grades for each student |
| Email regex validation | ✅ | Pattern matching for email format |
| Count grades > 90 | ✅ | Iterates and counts high grades |
| Comments throughout | ✅ | Code sections clearly documented |

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork the repository
- Experiment with additional features
- Suggest improvements via issues
- Share your learning journey

## 📄 License

This project is created for educational purposes as part of Coding Temple's curriculum.

## 👨‍💻 Author

Created as part of the Object-Oriented Python Practice assignment.

---

**Date**: January 2026  
**Course**: Coding Temple - Python Programming  
**Topic**: Object-Oriented Programming & Data Structures
