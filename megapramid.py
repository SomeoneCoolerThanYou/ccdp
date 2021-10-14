
n = int(input('Rows = '))
i = 1
for i in range(n):
    for j in range(i, n ):
        print(chr(ord('A') - 1 + j), end = ' ')
    print()
