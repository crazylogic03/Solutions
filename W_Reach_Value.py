# import sys
# sys.setrecursionlimit(10**7)

def can_reach(n):
    if n == 1:
        return True
    
    if n % 10 == 0 and can_reach(n // 10):
        return True
    
    if n % 20 == 0 and can_reach(n // 20):
        return True
    
    return False
t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if can_reach(n) else "NO")