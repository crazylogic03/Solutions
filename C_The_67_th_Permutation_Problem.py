t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in range(1, n + 1):
        res.append(i)
        res.append(i + n)
        res.append(i + 2 * n)
    print(*res)