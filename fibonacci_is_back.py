f = [1,1]
n = int(input("YOOOO\n>"))
i = 1
while i <= n:
    add = f[i-1] + f[i]
    f.append(add)
    i+=1
print(f)
