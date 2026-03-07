a, b = map(int, input().split())
if a + b > 0 and abs(a - b) <= 1:
    print("YES")
else:
    print("NO")