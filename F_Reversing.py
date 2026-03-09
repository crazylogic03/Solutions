n=int(input())
arr=list(map(int,input().split()))
new=[]
for i in range(n-1,-1,-1):
    new.append(arr[i])
print(*new)
