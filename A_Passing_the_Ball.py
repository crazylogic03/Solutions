t=int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left_R = 0
    while left_R < n and s[left_R] == 'R':
        left_R += 1
    right_L = 0
    while right_L < n and s[n - 1 - right_L] == 'L':
        right_L += 1
    print(left_R + right_L)