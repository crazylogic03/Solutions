def numbe(n):
    if n==0:
        return 
    if n==1:
        print(n)
    else:
        print(n,end=" ")
        numbe(n-1)
n=int(input())
numbe(n)