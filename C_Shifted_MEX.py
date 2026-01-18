t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(set(arr))
    # print(arr)
    best=0
    count=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            count+=1
        else:
            best=max(best,count)
            count=1
    best=max(best,count)
    print(best)
