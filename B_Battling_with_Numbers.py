MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))
 
i=j=0
count= 0
flag=True
 
while i < N or j < M:
    if j==M or (i<N and A[i]<C[j]):
        a=B[i]
        b=0
        i+=1
    elif i == N or (j < M and C[j] < A[i]):
        flag=False
        break
    else:
        a=B[i]
        b=D[j]
        i+=1
        j+=1
    if b > a:
        flag=False
        break
    if a > b:
        count += 1
 
if not flag:
    print(0)
else:
    print(pow(2, count, MOD))