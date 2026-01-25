t=int(input())
for _ in range(t):
    n,s,x=map(int,input().split())
    a=list(map(int,input().split()))
    tot=sum(a)
    if tot<= s and (s-tot) % x == 0:
        print("YES")
    else:
        print("NO")