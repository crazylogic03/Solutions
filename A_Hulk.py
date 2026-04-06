n = int(input())
result = ""
for i in range(1,n+1):
    if i % 2 == 1:
        result+="I hate"
    else:
        result += "I love"
    if i == n:
        result+=" it"
    else:
        result += " that "

print(result)