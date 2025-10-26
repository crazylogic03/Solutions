def countperformances(n, scores):
    if n == 1:
        return 0  

    amazing_count = 0
    best = scores[0]
    worst = scores[0]

    for i in range(1, n):
        if scores[i] > best:
            best = scores[i]
            amazing_count += 1
        elif scores[i] < worst:
            worst = scores[i]
            amazing_count += 1

    return amazing_count
n = int(input())  
scores = list(map(int, input().split()))
print(countperformances(n, scores))
