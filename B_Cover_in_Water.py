t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    segments = []
    i = 0

    while i < n:
        if s[i] == '.':
            j = i
            while j < n and s[j] == '.':
                j += 1
            segments.append(j - i)
            i = j
        else:
            i += 1
    if len(segments) == 1:
        L = segments[0]
        print(min(2, L))
    else:
        ans = 0
        for L in segments:
            if L == 1:
                ans += 1
            else:
                ans += 2
        print(ans)