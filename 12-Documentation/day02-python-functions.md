# Day 2 – Python Functions

## 1. What is a Function?
A function is a reusable block of code that performs a specific task.

## 2. Function Syntax

```python
def function_name(parameters):
    # Statements
    return result
```

- `def`: Defines a function.
- Function name: Identifies the function.
- Parameters: Inputs provided to the function.
- `return`: Sends the result back.

## 3. Example: Addition

```python
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(10, 20))
```

Output: `30`

## 4. Example: Calculate Average

```python
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

print(calculate_average(85, 90, 95))
```

Output: `90.0`

## 5. Example: Student Result Analyzer

```python
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

def check_result(a, b, c):
    if a >= 40 and b >= 40 and c >= 40:
        return "Pass"
    else:
        return "Fail"

marks1 = (85, 90, 95)
marks2 = (80, 30, 90)

print("Average:", calculate_average(*marks1))
print("Result:", check_result(*marks1))

print("Average:", calculate_average(*marks2))
print("Result:", check_result(*marks2))
```

## 6. Important Concepts Learned

- Functions and reusable code.
- Parameters and return statements.
- Calling one function from another.
- If-else conditions.
- Logical operator `and`.
- Debugging Python programs.
- Tuple unpacking using `*`.

## 7. Key Learning

The `and` operator checks whether all specified conditions are true.

For a student to pass, every subject must have at least 40 marks.

## 8. Day 2 Progress

- [x] Learned Python functions.
- [x] Practiced function parameters and return.
- [x] Built a Student Result Analyzer.
- [x] Practiced conditional statements.
- [x] Debugged logical errors.
- [ ] Python Lists
- [ ] Tuples, Sets and Dictionaries
- [ ] OOP
- [ ] File Handling
- [ ] Exception Handling
- [ ] Mini Project: Student Data Analyzer
