import math

a = []
m = len(matrix)
n = len(matrix[0])

if m == 1:
    for j in range(n):
        a.append(matrix[0][j])
    print(a)

elif n == 1:
    for i in range(m):
        a.append(matrix[i][0])
    print(a)

elif m % 2 == 1 and m == n:
    print(a)

elif m % 2 == 0 and m == n:
    print(a)

else:
    mod = math.ceil((m*n)/4)
    odd_count = 0
    even_count = 0

    for count in range(mod):
        if count % 2 == 0:
            for j in range(even_count, n - even_count):
                a.append(matrix[even_count][j])
            for i in range(even_count + 1, (m - 1) - even_count):
                a.append(matrix[i][-1 - even_count])
            even_count += 1

        else:
            for j in range(-1 - odd_count, odd_count - (n + 1), -1):
                a.append(matrix[-1 - odd_count][j])
            for i in range((m - 2) - odd_count, odd_count, -1):
                a.append(matrix[i][odd_count])
            odd_count += 1

    print(a)