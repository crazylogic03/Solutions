t = int(input())
for _ in range(t):
    x = input()
    digits = [int(d) for d in x]
    s=sum(digits)
    if s <= 9:
        print(0)
        continue
    rem=s-9
    digits.sort(reverse=True)
    mov=0
    count=0
    for i in digits:
        count+=i
        mov+=1
        if count>=rem:
            break
    print(mov)
