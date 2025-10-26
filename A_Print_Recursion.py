def recurse(n):
    if n==0:
        return 
    print("I love Recursion")
    recurse(n-1)
n=int(input())
recurse(n)