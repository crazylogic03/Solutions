t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(n):
        current_max = arr[i]
        for j in range(i, n):
            current_max = max(current_max, arr[j])
            ans.append(current_max)

    print(*ans)