d = int(input())
s = str(d)
L = len(s)
result = []
for i in range(d):
    result.append(s)
    if i != d - 1:
        result.append('0')
print(''.join(result))