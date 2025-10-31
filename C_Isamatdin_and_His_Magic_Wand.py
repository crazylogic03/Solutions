t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    has_even = False

    
    has_odd = False
    
    for x in a:
        if x % 2 == 0:
            has_even = True
        else:
            has_odd = True
    
    if has_even and has_odd:
        a.sort()
    
    print(*a)
