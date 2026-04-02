n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

pow2 = [1] * 51
for i in range(1, 51):
    pow2[i] = pow2[i - 1] * 2

ans = 0

for i in range(n):
    cnt0 = a[i].count(0)
    cnt1 = a[i].count(1)
    ans += (pow2[cnt0] - 1)
    ans += (pow2[cnt1] - 1)

for j in range(m):
    cnt0 = 0
    cnt1 = 0
    for i in range(n):
        if a[i][j] == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    ans += (pow2[cnt0] - 1)
    ans += (pow2[cnt1] - 1)
ans -= n * m
print(ans)