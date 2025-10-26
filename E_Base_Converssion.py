def bin(n):
    if n==0:
        return 
    if n>0:
        bin(n//2)
        print(n%2,end="")
t=int(input())
for _ in range(t):
    n=int(input())
    bin(n)
    print()