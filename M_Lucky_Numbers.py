a, b = map(int, input().split())
lis = []
for i in range(a, b + 1):
    s = str(i)
    if all(ch == '4' or ch == '7' for ch in s):
        lis.append(i)
if len(lis) > 0:
    print(*lis)
else:
    print(-1)