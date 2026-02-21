X = input()

if '0' <= X <= '9':
    print("IS DIGIT")
else:
    print("ALPHA")
    if 'A' <= X <= 'Z':
        print("IS CAPITAL")
    else:
        print("IS SMALL")