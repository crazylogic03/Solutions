t = int(input())
results = []
for _ in range(t):
    n = int(input())
    if n == 2:
        results.append(2)
    elif n == 3:
        results.append(3)
    elif n % 2 == 0:
        results.append(0)
    else:
        results.append(1)
print('\n'.join(map(str, results)))