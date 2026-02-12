n=int(input())
year=n//365
n%=365

months=n//30
n%=30

days =n

print(f"{year} years")
print(f"{months} months")
print(f"{days} days")