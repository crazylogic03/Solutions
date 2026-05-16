t = int(input())

for _ in range(t):
    n=int(input())
    w=list(map(int, input().split()))
    c0=w.count(0)
    c1=w.count(1)
    c2=w.count(2)
    pair=min(c1, c2)
    rem = abs(c1 - c2)
    print(c0 + pair+rem // 3)