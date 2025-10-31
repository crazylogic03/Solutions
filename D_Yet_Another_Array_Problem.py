
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def smallest_x(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    
    if g == 1:
        return 2
    
    primes = prime_factors(g)
    
    x = 2
    while x <= 10**18:
        ok = True
        for p in primes:
            if x % p == 0:
                ok = False
                break
        if ok:
            return x
        x += 1
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(smallest_x(a))
