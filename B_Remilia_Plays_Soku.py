t=int(input())
for _ in range(t):
    n,x1,x2,k=map(int,input().split())
    m1= (x2 - x1 + n) % n
    m2= (x1 - x2 + n) % n
    

    ans = min(m1,m2)+k
    print(ans)
    # d1 = (x2 - x1 + n) % n
    # d2 = (x1 - x2 + n) % n

    # print(min(d1, d2) + k)