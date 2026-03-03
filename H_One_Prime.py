import math
X = int(input())
is_prime = True
if X <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO")