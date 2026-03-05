while True:
    N, M = map(int, input().split())
    if N <= 0 or M <= 0:
        break
    start = min(N, M)
    end = max(N, M)
    total = 0
    numbers = []
    for i in range(start, end + 1):
        numbers.append(str(i))
        total += i
    print(" ".join(numbers) + f" sum ={total}")


    