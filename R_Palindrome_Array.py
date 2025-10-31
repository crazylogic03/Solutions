def is_palindrome(A, left, right):
    if left >= right:
        return True
    if A[left] != A[right]:
        return False
    return is_palindrome(A, left + 1, right - 1)
N = int(input())
A = list(map(int, input().split()))
if is_palindrome(A, 0, N - 1):
    print("YES")
else:
    print("NO")


