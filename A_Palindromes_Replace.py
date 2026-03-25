s = list(input())
n = len(s)
possible = True

for i in range(n // 2):
    j = n - 1 - i
    
    if s[i] == s[j]:
        if s[i] == '?':
            s[i] = s[j] = 'a'
    else:
        if s[i] == '?':
            s[i] = s[j]
        elif s[j] == '?':
            s[j] = s[i]
        else:
            possible = False
            break
if possible and n % 2 == 1 and s[n // 2] == '?':
    s[n // 2] = 'a'

if not possible:
    print(-1)
else:
    print("".join(s))