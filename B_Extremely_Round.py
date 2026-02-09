t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    power=1
    while power<=n:
        for i in range(1,10):
            if i*power<=n:
                ans+=1
        power*=10
    print(ans)