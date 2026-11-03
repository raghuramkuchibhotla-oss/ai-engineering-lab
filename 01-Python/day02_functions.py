# /*
# # def calculate_average(a, b, c):
#     total = a + b + c
#     average = total / 3
#     return average


# student_average = calculate_average(85, 90, 95)

# print("Student Average:", student_average)

# def result(a, b, c):
#     average = (a + b + c) / 3

#     if average >= 40:
#         return "Pass"
#     else:
#         return "Fail"


# print("Result:", result(85, 90, 95))
# print("Result:", result(20, 30, 25))
    
    
# def result(a,b,c):
#     students_average = calculate_average(80, 85, 90)
#     students_subjects_average = caluculate_subjects_average(80, 30, 90)
#     average = (a + b + c) / 3
#     subjects = (a + b + c) / 3
    
#     if average >= 40:
#         return "Pass"
#     elif average < 40:
#         return "Fail"
#     elif subjects >=40:
#         return "Pass"
#     elif subjects <= 40:
#         return "Fail"
#     #else:
#         return "Invalid input"

#     #print("Result:", result(80, 30, 90))
# /*
    
# def calculate_average(a, b, c):
#     average = (a + b + c) / 3
#     return average
# def calculate_subjects_average(a, b, c):
#     subjects_average = (a + b + c) / 3
#     return subjects_average
 
#     if calculate_average(a, b, c) >= 40:
#         return "Pass"
#     else:
#         return "Fail"
    
#     if calculate_subjects_average(a, b, c) >= 40:
#         return "Pass"
#     else:
#         return "Fail"
    
#     print("Result:", result(80, 30, 90))
#     print("Result:", result(80, 85, 90))

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average


def check_result(a, b, c):
    
    if a >= 40 and b >= 40 and c >= 40:
            return "Pass"
    else:
            return "Fail"
       

    # Write your if-else condition here
    if calculate_average(a, b, c) >= 40:
        return "Pass"
    else:
        return "Fail"
   
# Test cases
marks1 = (85, 90, 95)
marks2 = (80, 30, 90)

print("Average:", calculate_average(*marks1))
print("Result:", check_result(*marks1))

print("Average:", calculate_average(*marks2))
print("Result:", check_result(*marks2))