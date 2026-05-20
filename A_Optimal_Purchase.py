t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    full = n // 3
    rem = n % 3
    ans = full * min(3 * a, b) + min(rem * a, b)
    print(ans)

    