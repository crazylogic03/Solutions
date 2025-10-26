def log2(n):
    if n==1:
        return 0 
    return 1 + log2(n//2)
n=int(input())
print(log2(n))