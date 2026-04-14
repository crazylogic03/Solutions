def is_odd(n):
    return n % 2 != 0
def is_binary_palindrome(n):
    binary = bin(n)[2:]
    return binary == binary[::-1]
n = int(input())

if is_odd(n) and is_binary_palindrome(n):
    print("YES")
else:
    print("NO")