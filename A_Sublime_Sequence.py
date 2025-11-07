t=int(input())
for _ in range(t):
    x,n=list(map(int,input().split()))
    arr=[]    
    for i in range(n):
        if i%2==0:
            arr.append(x)
        else:
            arr.append(-x)
    print(sum(arr))
