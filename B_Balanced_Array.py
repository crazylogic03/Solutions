t = int(input())
for _ in range(t):
    n = int(input())
    k = n // 2
    if k % 2 != 0:
        print("NO")
    else:
        print("YES")
        evens = [2*i for i in range(1, k+1)]
        odds = [2*i-1 for i in range(1, k)]
        odds.append(2*k - 1 + k)
        ans = evens + odds
        print(*ans)
