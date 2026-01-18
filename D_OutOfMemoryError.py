t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    orig=list(map(int,input().split()))
    cur=orig[:]
    for _ in range(m):
        b,c=map(int,input().split())
        b -= 1
        cur[b] += c
        if cur[b] > h:
            cur = orig[:]
    print(*cur)
