def f(x):
    x += 1
    while x % 10 == 0:
        x //= 10
    return x
def reachable_numbers(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = f(n)
    return len(seen)
n = int(input())
print(reachable_numbers(n))
