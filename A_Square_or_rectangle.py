t=int(input())
for _ in range(t):
    l,b=map(int,input().split())
    if l==b:
        print("Square")
    else:
        print("Rectangle")
