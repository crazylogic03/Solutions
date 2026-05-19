t = int(input())
for _ in range(t):
    a_str, n_str = input().split()
    n = int(n_str)
    d1, d2 = map(int, input().split())
    
    a = int(a_str)
    L = len(a_str)
    
    candidates = set()
    candidates.add(d1)
    candidates.add(d2)
    if L > 1:
        if d2 > 0:
            candidates.add(int(str(d2) * (L - 1)))
    if d1 > 0:
        candidates.add(int(str(d1) * (L + 1)))
    else:
        candidates.add(int(str(d2) + str(d1) * L))
    for i in range(L):
        prefix = a_str[:i]
        
        for x in (d1, d2):
            if i == 0 and x == 0 and L > 1:
                continue 
            
            val_x = x
            val_a = int(a_str[i])
            
            if val_x < val_a:
                cand_str = prefix + str(x) + str(d2) * (L - 1 - i)
                candidates.add(int(cand_str))
            elif val_x > val_a:
                cand_str = prefix + str(x) + str(d1) * (L - 1 - i)
                candidates.add(int(cand_str))
        if int(a_str[i]) not in (d1, d2):
            break
    else:
        candidates.add(a)
    min_diff = min(abs(a - c) for c in candidates)
    print(min_diff)