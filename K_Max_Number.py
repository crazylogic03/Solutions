n=int(input())
arr=list(map(int,input().split()))
def maxnum(n,maxa):
    if n==len(arr):
        return maxa
    maxa = max(maxa,arr[n])
    return maxnum(n+1,maxa)
print(maxnum(0,arr[0]))    
