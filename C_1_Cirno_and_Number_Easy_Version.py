t = int(input())

for _ in range(t):
    a, n = map(int, input().split())
    digits = sorted(map(str, input().split()))

    s = str(a)
    L = len(s)

    ans = [float('inf')]
    def dfs(pos, length, tight, started, cur):

        if started:
            val = int(cur)
            ans[0] = min(ans[0], abs(a - val))

        if pos == length:
            return
        limit = s[pos] if tight and pos < L else '9'

        for d in digits:

            if tight and d > limit:
                break
            if not started and length > 1 and d == '0':
                continue

            ntight = tight and (d == limit)

            dfs(
                pos + 1,
                length,
                ntight,
                True,
                cur + d
            )
    for length in [L - 1, L, L + 1]:
        if length > 0:
            dfs(0, length, length == L, False, "")

    print(ans[0])