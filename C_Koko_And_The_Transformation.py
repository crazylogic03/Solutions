data = list(map(int, input().split()))
n, m = data[0], data[1]
a = data[2:2+n]
b = data[2+n:2+n+m]

if sum(a) == sum(b):
    print("Yes")
else:
    print("No")