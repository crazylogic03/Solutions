n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (k * l) // nl
limes = c * d
salt = p // np
total_toasts = min(drink, limes, salt)
print(total_toasts // n)