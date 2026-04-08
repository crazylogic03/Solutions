n, m, k = map(int, input().split())
x = min(n // 2, m, k)
n -= 2 * x
m -= x
k -= x

y = min(n, m, k)
n -= y
m -= y
k -= y
z = min(n // 2, k)

print(x + y + z)