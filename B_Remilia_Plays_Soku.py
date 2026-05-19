t = int(input())
for _ in range(t):
    n, x1, x2, k = map(int, input().split())
    dist = abs(x1 - x2)
    min_dist = min(dist, n - dist)
    if n <= 3:
        print(min_dist)
    else:
        print(min_dist + k)