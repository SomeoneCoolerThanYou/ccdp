num = int(input("Enter the number: "))
x = int(num)
i = 3
f = 0
if num % 2 == 0:
    print("Not Prime")
elif (num-1)%6!=0 and (num+1)%6!=0:
    print("Not Prime")
else:
    for i in range(3, x):
        if num % i == 0:
            f += 1
            if f == 1:
                break
    if f == 0:
        print("Prime")
    else:
        print("Not Prime")
