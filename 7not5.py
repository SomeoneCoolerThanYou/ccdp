#Write a program which will find all such numbers which are divisible by 7
#but are not a multiple of 5,between 1500 and 2701 (both included).
i = 1500
while i <= 2701:
    condition = False
    if i%7 == 0:
        condition = True
    if i%5 == 0:
        condition = False
    if condition == True:
        print(i, end=' ')
    i+=1
