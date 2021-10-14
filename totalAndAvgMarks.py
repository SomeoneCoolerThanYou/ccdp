#WAP a program to input marks of 5 subjects, calculate and display total
#marks and average marks of a student.
total = 0
for i in range(1, 6):
    marks = int(input("Enter the marks of subject "+str(i) + " : "))
    total += marks
print("Total marks = ", total)
print("Average marks = ", total/5)
