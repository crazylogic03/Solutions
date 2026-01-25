t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c=[]
    for i in range(n):
        c.append(max(a[i],b[i]))
    suf=[0]*n
    mx=0
    for i in range(n-1,-1,-1):
        if c[i]>mx:
            mx=c[i]
        suf[i]=mx
        
    pre = [0]*(n+1)
    for i in range(n):
        pre[i+1]=pre[i]+suf[i]
        
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        res.append(pre[r]-pre[l - 1])
    print(*res)
