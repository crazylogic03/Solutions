t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    if arr[0] == arr[-1]:
        print("NO")
        continue
    
    res = []
    s = 0
    used = [False]*n
    
    ok = True
    
    for _ in range(n):
        found = False
        for i in range(n):
            if not used[i] and arr[i] != s:
                res.append(arr[i])
                s += arr[i]
                used[i] = True
                found = True
                break
        
        if not found:
            ok = False
            break
    
    if not ok:
        print("NO")
    else:
        print("YES")
        print(*res)