import sys
sys.setrecursionlimit(10**6)
def prefix_max(i, n, arr, current_max):
    if i == n:
        return
    current_max = max(current_max, arr[i])
    print(current_max, end=" ")
    
    prefix_max(i + 1, n, arr, current_max)
n = int(input())
arr = list(map(int, input().split()))

prefix_max(0, n, arr, float('-inf'))