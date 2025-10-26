n, k = map(int, input().split())
a = list(map(int, input().split()))

cutoff = a[k - 1]
count = sum(1 for score in a if score >= cutoff and score > 0)

print(count)
