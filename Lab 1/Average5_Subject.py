# 6. Find the average of the marks obtained in 5 subjects.

subject1 = float(input("Enter the marks obtained in subject 1: "))
subject2 = float(input("Enter the marks obtained in subject 2: "))
subject3 = float(input("Enter the marks obtained in subject 3: "))
subject4 = float(input("Enter the marks obtained in subject 4: "))
subject5 = float(input("Enter the marks obtained in subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5

print("The average marks obtained in 5 subjects is:", average_marks)
