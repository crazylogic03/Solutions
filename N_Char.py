X = input()
if 'a' <= X <= 'z':
    print(chr(ord(X) - 32))
else:
    print(chr(ord(X) + 32))
