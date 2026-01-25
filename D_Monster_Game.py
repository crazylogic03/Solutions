t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort(reverse=True)
    ans=0
    count=0
    for i in range(n):
        count+=b[i]
        if count>n:
            break
        val=a[count-1]*(i+1)
        if val>ans:
            ans=val
    print(ans)