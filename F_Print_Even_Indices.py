n=int(input())
arr=list(map(int,input().split()))
def evenind(arr,index):
    if index<0:
        return 
    print(arr[index],end=" ")
    evenind(arr,index-2)
if n%2==0:
    evenind(arr,n-2)
else:
    evenind(arr,n-1)