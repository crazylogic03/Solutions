n=int(input())
arr=list(map(int,input().split()))
mn = min(arr)
pos = arr.index(mn) + 1

print(mn, pos)