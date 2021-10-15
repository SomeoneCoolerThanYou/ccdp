#patterns
n = int(input("Enter no. of rows: "))
i = 1
j = 1
while i <= n:
    print('X'*i)
    i+=1
print("-----------------------------------------------------------")

for i in range(1,n+1):
    num_in_a_row = 1
    while num_in_a_row <= i:
        print(j,end=' ')
        j+=1
        num_in_a_row += 1
    print()
print("------------------------------------------------------------")
i = n
while i >= 0:
      print("X"*i)
      i-=1
print("-------------------------------------------------------------")
for i in range(n):
    s = n - i
    print("  "*i,"X"*s)
