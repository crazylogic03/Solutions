def some(n):
    if n>0:
        some(n-1)
        print(n)
n=int(input())
some(n)