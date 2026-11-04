student = ("Raghu ram", 20, "AIML", "KG REDDY COLLEGE")
print(student)
print(student[0])
print(student[3])
len(student)
print('Number of elements in the tuple:', len(student))

# Tuple unpacking
name, age, branch, college = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("College:", college)

# Marks tuple
marks = (85, 90, 75, 88, 95)

average = sum(marks) / len(marks)

print("Average marks:", average)