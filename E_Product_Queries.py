from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    exists=[0]*(n+1)
    for i in a:
        exists[i] = 1
    dp=[float("inf")]*(n+1)
    q = deque()
    for v in range(1, n + 1):
        if exists[v]:
            dp[v]=1
            q.append(v)
    while q:
        node=q.popleft()
        for v in range(2,n//node + 1):
            if exists[v]:
                neigh=node* v
                if dp[neigh]>dp[node] + 1:
                    dp[neigh]=dp[node] + 1
                    q.append(neigh)
    ans = []
    for i in range(1, n + 1):
        if dp[i]!=float("inf"):
            ans.append(dp[i])
        else:
            ans.append(-1)
    print(*ans)
