t = int(input())
results = []
for _ in range(t):
    s,k,m=map(int,input().split())
    if s<=k:
        if m%k==0:
            results.append(s)
        else:
            le=m%k
            results.append(max(0,s-le))
    else:
        n=m//k
        r=m%k
        if n%2==0:
            results.append(s-r)
        else:
            results.append(k-r)
for x in results:
    print(x)
