k,r=map(int,input().split())
ans=[]
for i in range(1,11):
    if (i * k) % 10 == 0 or (i * k) % 10 == r:
        ans.append(i)
print(ans[0])

