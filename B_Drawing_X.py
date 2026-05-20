n = int(input())

for i in range(n):
    row = ['*'] * n

    row[i] = '\\'
    row[n - i - 1] = '/'

    if i == n // 2:
        row[i] = 'X'

    print(''.join(row))