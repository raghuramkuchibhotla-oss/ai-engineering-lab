students_id={101,102,103,104,102,101,105}
print("Students Ids:",students_id)

students_id.add(106)
print(students_id)

students_id.remove(104)
print(students_id)

Total_students=len(students_id)
print("Total Students:",Total_students)

###

A={101,102,103,104}
B={103,104,105,106}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))