from collections import deque

n = int(input())
a = list(map(int, input().split()))

dq = deque()
rev = False

for x in a:
    if x == 0:
        rev = not rev
        if rev:
            dq.appendleft(0)
        else:
            dq.append(0)
    else:
        if rev:
            dq.appendleft(x)
        else:
            dq.append(x)

if rev:
    dq.reverse()

print(*dq)