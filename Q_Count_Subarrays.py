t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    length = 1
    ans = 1  
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            length += 1
        else:
            length = 1
        
        ans += length
    
    print(ans)