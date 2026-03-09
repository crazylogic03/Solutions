n = int(input())
arr = list(map(int, input().split()))
pali = True
for i in range(n // 2):
    if arr[i] != arr[n - 1 - i]:
        pali = False
        break
if pali:
    print("YES")
else:
    print("NO")