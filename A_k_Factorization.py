n,k=map(int, input().split())
div=[]
a=n
i=2
while i*i<=a:
    while a% i==0:
        if len(div)<k-1:
            div.append(i)
            a//= i
        else:
            break
    i += 1
if a> 1:
    div.append(a)
if len(div) == k:
    print(*(div))
else:
    print(-1)