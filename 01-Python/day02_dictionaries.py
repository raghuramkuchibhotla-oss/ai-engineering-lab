Student = {
    "name": "veeraraghvan",
    "age": 20,
    "branch": "AIML",
    "marks":95,
}

print(Student)
print(Student["name"])
print(Student["branch"])

Student["Year:"] = 2
Student.update(marks=98)
print(Student)

# Print all keys
print(Student.keys())

# Print all values
print(Student.values())

# Print all key-value pairs
for key, value in Student.items():
    print(key, ":", value)