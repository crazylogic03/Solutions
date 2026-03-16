MOD = 998244353
n, k = map(int,input().split())
dp = [1] * (n + 1)
for _ in range(k - 1):
    new = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i * 2, n + 1, i):
            new[j] = (new[j] + dp[i]) % MOD
    dp = new
print(sum(dp) % MOD)