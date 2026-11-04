# AI Engineering Lab — Day 2 Learning Report

**Date:** 4 November 2026  
**Focus:** Python Fundamentals and Object-Oriented Programming  
**Status:** In Progress

## 1. Learning Objectives

- Understand Python functions and reusable code.
- Learn Python data structures.
- Understand Object-Oriented Programming (OOP).
- Practice writing and executing Python programs.
- Maintain code and learning documentation on GitHub.

## 2. Topics Completed

### A. Python Functions

Learned:
- Defining functions using `def`.
- Parameters and arguments.
- Returning values using `return`.
- Calling functions.
- Conditional statements inside functions.
- Logical operators such as `and`.
- Tuple unpacking when passing arguments.

Example:

```python
def calculate_average(a, b, c):
    return (a + b + c) / 3


def check_result(a, b, c):
    if a >= 40 and b >= 40 and c >= 40:
        return "Pass"
    return "Fail"


marks = (85, 90, 95)

print("Average:", calculate_average(*marks))
print("Result:", check_result(*marks))
```

### B. Lists

Learned:
- Creating lists.
- Accessing elements using indexing.
- Adding elements with `append()` and `insert()`.
- Removing elements with `remove()` and `pop()`.
- Sorting using `sort()`.
- Calculating totals and averages using `sum()` and `len()`.
- Lists are mutable.

### C. Tuples

Learned:
- Creating tuples.
- Accessing elements using indexing.
- Using `len()`, `sum()`, `min()` and `max()`.
- Tuple unpacking.
- Tuples are immutable.

### D. Sets

Learned:
- Creating sets.
- Removing duplicate values automatically.
- Adding and removing elements.
- Set operations:
  - Union
  - Intersection
  - Difference

### E. Dictionaries

Learned:
- Creating key-value pairs.
- Accessing values using keys.
- Adding and updating values.
- Using `keys()`, `values()` and `items()`.
- Iterating through dictionaries.
- Dictionaries are mutable.

## 3. Object-Oriented Programming (OOP) — In Progress

Learned so far:

- **Class:** A blueprint used to create objects.
- **Object:** An instance of a class.
- **Constructor:** `__init__()` initializes an object.
- **self:** Refers to the current object.
- **Attributes:** Store information about an object.
- **Methods:** Functions defined inside a class.

### Practical Example — Chatbot Class

```python
class Chatbot:

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print("Hello! I am", self.name)
        print("I am powered by", self.model)


chatbot1 = Chatbot("LOOMA", "GPT")
chatbot2 = Chatbot("Raghu AI", "Custom Model")

chatbot1.introduce()
chatbot2.introduce()
```

### Expected Output

```text
Hello! I am LOOMA
I am powered by GPT
Hello! I am Raghu AI
I am powered by Custom Model
```

Remaining OOP topics:
- Encapsulation
- Inheritance
- Practical Student Management System

## 4. Key Learning Outcomes

By the end of this learning session, I understood:

1. How to organize reusable code using functions.
2. The differences between lists, tuples, sets and dictionaries.
3. How Python stores and manages structured data.
4. How classes and objects work.
5. How constructors initialize objects.
6. How methods perform actions using object attributes.

## 5. Day 2 Progress Tracker

- [x] Python Functions
- [x] Lists
- [x] Tuples
- [x] Sets
- [x] Dictionaries
- [ ] Complete OOP
- [ ] File Handling
- [ ] CSV Processing
- [ ] Exception Handling
- [ ] Modules and Project Organization
- [ ] Student Data Analyzer Mini-Project

## 6. Next Learning Session

Continue with:
1. OOP revision and practical exercises.
2. Encapsulation and inheritance.
3. Student Management System.
4. File handling and CSV.
5. Exception handling.
6. Python modules and project organization.
7. Student Data Analyzer mini-project.

**Day 2 Summary:** Successfully learned Python functions and four important data structures, and started Object-Oriented Programming with a practical chatbot example.

**Project:** AI Engineering Lab  
**Repository:** https://github.com/raghuramkuchibhotla-oss/ai-engineering-lab