t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    for i in range(n):
        mx=n-i
        if a[i]!=mx:
            posi=a.index(mx)
            a[i:posi+1]=reversed(a[i:posi+1])
            break
    print(*a)