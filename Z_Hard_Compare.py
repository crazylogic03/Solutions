import math
A, B, C, D = map(int, input().split())
if B * math.log(A) > D * math.log(C):
    print("YES")
else:
    print("NO")
