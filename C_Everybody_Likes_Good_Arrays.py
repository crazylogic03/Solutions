t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    operations = 0
    i = 0
    
    while i < n:
        j = i
        while j < n and (a[j] % 2) == (a[i] % 2):
            j += 1
        
        block_length = j - i
        operations += block_length - 1
        
        i = j
    
    print(operations)
