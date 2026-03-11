t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans = float('inf')
    mini = arr[0] - 1
    for j in range(1, n):
        ans = min(ans, mini + arr[j] + (j + 1))
        mini = min(mini, arr[j] - (j + 1))
    print(ans)