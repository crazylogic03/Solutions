t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k>=31:
        print(n+1)
    else:
        print(min(n + 1, pow(2, k)))