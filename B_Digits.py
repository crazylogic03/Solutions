import math
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    res = []
    res.append(1)
    if n >= 3 or (n == 2 and d % 3 == 0):
        res.append(3)
    if d == 5:
        res.append(5)
    if n >= 3 or (n == 2 and d == 7):
        res.append(7)
    if n >= 6:
        res.append(9)
    else:
        L = math.factorial(n)
        if (L * d) % 9 == 0:
            res.append(9)
    print(*res)
