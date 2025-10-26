def numb(n):
    if n<10:
        print(n,end=" ")
        return 
    numb(n//10)
    print(n%10,end=" ")  

t=int(input())
for _ in range(t):
    n=int(input())
    numb(n)
    print()



