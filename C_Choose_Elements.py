n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = 0
for i in range(k):
    if a[i] > 0:
        total += a[i]
    else:
        break

print(total)