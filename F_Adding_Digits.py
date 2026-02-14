a, b, n = map(int, input().split())

remainder = a % b
result = str(a)

for _ in range(n):
    found = False
    for d in range(10):
        if (remainder * 10 + d) % b == 0:
            result += str(d)
            remainder = 0
            found = True
            break
    if not found:
        print(-1)
        break
else:
    print(result)
