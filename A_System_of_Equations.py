n, m = map(int, input().split())
count = 0
for i in range(32): 
    b = n - i * i
    if b >= 0 and i + b * b == m:
        count += 1

print(count)
