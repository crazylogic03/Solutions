import math
X, P = map(float, input().split())
original = P / (1 - X / 100)
original = math.ceil(original * 100) / 100

print(f"{original:.2f}")
