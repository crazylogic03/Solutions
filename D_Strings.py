s=input()
t=input()

print(len(s),len(t))
print(s+t)

s0 = s[0]
t0 = t[0]
s = t0 + s[1:]
t = s0 + t[1:]

print(s,t)
