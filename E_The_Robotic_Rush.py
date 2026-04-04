t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = input()

    a.sort()
    b.sort()

    pref = 0
    min_pref = 0
    max_pref = 0

    dead = [False] * n
    res = []

    for ch in s:
        if ch == 'R':
            pref += 1
        else:
            pref -= 1

        min_pref = min(min_pref, pref)
        max_pref = max(max_pref, pref)

        j = 0
        alive = 0

        for i in range(n):
            if dead[i]:
                continue

            left = a[i] + min_pref
            right = a[i] + max_pref
            while j < m and b[j] < left:
                j += 1
            if j < m and b[j] <= right:
                dead[i] = True
            else:
                alive += 1

        res.append(alive)

    print(*res)