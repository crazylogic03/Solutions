n=int(input())
arr=list(map(int,input().split()))
mn = min(arr)
freq = arr.count(mn)
if freq%2==0:
    print("Unlucky")
else:
    print("Lucky")
