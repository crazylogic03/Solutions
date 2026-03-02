a,b = map(int,input().split())
lis=[]
for i in range(a,b+1):
    i=str(i)
    sp = i.split()
    if ("4"in sp) or ("7" in sp):
        lis.append(int(i))
if len(lis)>0:
    print(*lis)
else:
    print(-1)
    