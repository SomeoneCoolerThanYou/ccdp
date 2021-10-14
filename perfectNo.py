num=int(input("Enter the number: "))
sum = 0
for i in range(1, num):
    if num%i==0:
        sum+=i
if num == sum:
    print("Perfect")
else:
    print("Not Perfect")
