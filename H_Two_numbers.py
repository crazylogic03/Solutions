import math
a,b=map(int,input().split())
print(f"floor {a} / {b} = {math.floor(a/b)}")
print(f"ceil {a} / {b} = {math.ceil(a/b)}")
print(f"round {a} / {b} = {math.floor(a/b)+1 if a/b-math.floor(a/b)>=0.5 else math.floor(a/b)}")