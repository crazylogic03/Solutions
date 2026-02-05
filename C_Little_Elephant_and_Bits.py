s = input()
for i in range(len(s)):
    if s[i] == '0':
        print(s[:i] + s[i+1:])
        break
else:
    print(s[:-1])
