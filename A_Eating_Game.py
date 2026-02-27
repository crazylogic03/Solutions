t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    winners_found = []
    for start_pos in range(n):
        temp_dishes = list(a)
        eaten = 0
        current = start_pos
        while eaten < total_sum:
            if temp_dishes[current] > 0:
                temp_dishes[current] -= 1
                eaten += 1
                if eaten == total_sum:
                    winner = current + 1
                    if winner not in winners_found:
                        winners_found.append(winner)
                    break
            current = (current + 1) % n
    print(len(winners_found))