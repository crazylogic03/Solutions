def max_odd_sum_subsequence(arr):
    even = 0
    odd = float('-inf')
    for x in arr:
        if x % 2 == 0:
            even = max(even, even + x)
            odd = max(odd, odd + x)
        else:
            new_even = max(even, odd + x)
            new_odd = max(odd, even + x)
            even, odd = new_even, new_odd

    return odd
n=int(input())
arr=list(map(int,input().split()))
print(max_odd_sum_subsequence(arr))
