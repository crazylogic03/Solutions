n = input()
count = n.count('4') + n.count('7')
if count > 0 and all(c in '47' for c in str(count)):
    print("YES")
else:
    print("NO")
