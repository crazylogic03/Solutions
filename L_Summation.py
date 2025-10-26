n=int(input())
arr=list(map(int,input().split()))
def summ(index,arr):
    if index==n:
        return 0
    return arr[index] + summ(index+1,arr)
print(summ(0,arr))