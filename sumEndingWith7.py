#WAP to input N numbers , calculate and display sum
#of those numbers whose last digit is 7.

n = int(input("The no of numbers you're going to input= "))
sum = 0
for i in range(n):
    num = int(input("Enter the number: "))
    for j in str(num):
        k = j
    if k == '7':
        sum += num
print(sum)
