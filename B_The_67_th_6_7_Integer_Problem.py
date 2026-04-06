t=int(input())
for _ in range(t):
    lis = list(map(int,input().split()))
    lis.sort()
    count=0
    for i in range(6):
        count+=(-lis[i])
    count+=lis[6]
    print(count)
    # print(lis)
    # a1,a2,a3,a4,a5,a6,a7=map(int,input().split())
    # lis=[]
    # list.appe

