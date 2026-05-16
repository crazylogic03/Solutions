t = int(input())
def generate(length, digits):
    res = []
    def dfs(cur):
        if len(cur) == length:
            if length == 1 or cur[0] != '0':
                res.append(int(cur))
            return

        for d in digits:
            dfs(cur + str(d))
    dfs("")
    return res

for _ in range(t):
    a, n = map(int, input().split())
    digits = list(map(int, input().split()))
    s = str(a)
    L = len(s)
    ans = 10**18
    for length in range(1, L + 2):
        nums = generate(length, digits)

        for b in nums:
            ans = min(ans, abs(a - b))

    print(ans)