A, B = map(int, input().split())
S = input()
if S[A] != '-':
    print("No")
else:
    ok = True
    for i in range(len(S)):
        if i == A:
            continue
        if not S[i].isdigit():
            ok = False
            break
    print("Yes" if ok else "No")