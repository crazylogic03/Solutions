n=int(input())
arr=list(map(int,input().split()))
tar=int(input())
if tar in arr:
    ind = arr.index(tar)
else:
    ind = -1
print(ind)