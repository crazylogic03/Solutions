a,s,b=map(str,input().split())
a=int(a)
b=int(b)
if s==">":
    if a>b:
        print("Right")
    else:
        print("Wrong")
elif s=="=":
    if a==b:
        print("Right")
    else:
        print("Wrong")
elif s=="<":
    if a<b:
        print("Right")
    else:
        print("Wrong")