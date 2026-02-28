n = input()
reversed_n = n[::-1]
trimmed = reversed_n.lstrip('0')
if trimmed == "":
    trimmed = "0"

print(trimmed)
if n == reversed_n:
    print("YES")
else:
    print("NO")