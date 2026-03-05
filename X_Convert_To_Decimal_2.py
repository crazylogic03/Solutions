t = int(input())

for _ in range(t):
    n = int(input())
    
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    
    result = (2 ** count) - 1
    print(result)