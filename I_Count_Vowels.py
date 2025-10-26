s=input()
vowels= ['a', 'e', 'i', 'o', 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
def vo(s,n,count):
    if n==len(s):
        return count
    if s[n] in vowels:
        count+=1
    return vo(s,n+1,count)
print(vo(s,0,0))
    