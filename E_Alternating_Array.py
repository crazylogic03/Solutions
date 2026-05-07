n = int(input())
a = list(map(int, input().split()))

ops1 = 0
ops2 = 0 

for i in range(n):
    if i % 2 == 0:
        if a[i] < 0:
            ops1 += 1
    else:
        if a[i] > 0:
            ops1 += 1
    if i % 2 == 0:
        if a[i] > 0:
            ops2 += 1
    else:
        if a[i] < 0:
            ops2 += 1

print(min(ops1, ops2))