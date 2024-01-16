n = int(input("write number here: "))
result = ''

for i in range(1, n + 1):
    result = result + str(i)

print(result)

for i in range(1, n + 1):
    print(i, end='')
