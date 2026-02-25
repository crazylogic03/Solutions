t=int(input())
for _ in range(t):
    A,B,X,Y=map(int,input().split())
    trades = A // X
    result = A+B+trades*(Y-X)
    
    print(result)

