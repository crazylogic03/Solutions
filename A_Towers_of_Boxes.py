import math
t=int(input())
for _ in range(t):
    n,m,d = map(int,input().split())
    maxbox=(d//m) + 1
    ans = math.ceil(n/maxbox)
    print(ans)

