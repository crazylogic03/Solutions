import math
t = int(input())
for _ in range(t):
    n = int(input())
    
    maxi = 0
    ans = 1
    for y in range(1, n):
        current_val = math.gcd(n, y) + y
        if current_val >= maxi:
            maxi = current_val
            ans = y
            
    print(ans)