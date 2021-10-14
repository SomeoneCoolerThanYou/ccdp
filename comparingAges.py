#to input of age of 3 people by user and determine oldest and youngest among them
age1 =  input("Enter the age of the person A: ")
age2 = input("Enter the age of the person B: ")
age3 = input("Enter the age of the person C: ")

print("The ages of the persons are arranged in the decreasing order as follows: ")
if age1>age2 and age1>age3:
    if age2>age3:
        print("A is the oldest, C is the youngest")
    elif age3>age2:
        print("A is the oldest, B is the youngest")
if age2>age3 and age2>age1:
    if age1>age3:
        print("B is the oldest, C is the youngest")
    elif age3>age1:
        print("B is the oldest, A is the youngest")
if age3>age2 and age3>age1:
    if age1>age2:
        print("C is the oldest, B is the youngest")
    elif age2>age1:
        print("C is the oldest, A is the youngest")
