#to assign stream to a student(assuming maximum marks in each subject = 100)
eng = int(input("Enter the student's marks in English: "))
math = int(input("Enter the student's marks in Mathematics: "))
sci = int(input("Enter the student's marks in Science: "))

stream = 'The student is eligible for the following stream(s): \n'

if (eng + math + sci)/3 >= 60:
    stream = stream + 'Commerce\n'
if (eng + sci)/2 >= 80 and math >= 60:
        stream = stream + 'Bio. Science\n'
if (eng + math + sci)/3 >= 80:
        stream = stream + 'Pure Science\n'
else:
    print("The student is not eligible for any stream")
    stream = ''
print()
print(stream)
