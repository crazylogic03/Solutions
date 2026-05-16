t = int(input())

for _ in range(t):
    n, x1, x2, k = map(int, input().split())

    d1 = (x2 - x1 + n) % n
    d2 = (x1 - x2 + n) % n

    d = min(d1, d2)

    if n % 2 == 0 and d == n // 2:
        print(max(d - 1, k + 1))
    else:
        print(max(d, k + 1))