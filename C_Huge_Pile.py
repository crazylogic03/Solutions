# Read the number of test cases
t_str = input()
if t_str:
    t = int(t_str)
    for _ in range(t):
        line = input().split()
        if not line:
            continue
        n, k = map(int, line)

        # Base case: if the starting pile is already k
        if n == k:
            print(0)
            continue

        current_level = {n}
        seen = {n}
        minutes = 0
        found = False

        # Continue as long as there are piles left to split
        while current_level:
            minutes += 1
            next_level = set()
            
            for x in current_level:
                # Calculate the two new pile sizes
                p1 = x // 2
                p2 = (x + 1) // 2
                
                for child in [p1, p2]:
                    if child == k:
                        found = True
                        break
                    # We only care about piles > 0 and those we haven't seen at an earlier time
                    if child > 0 and child not in seen:
                        next_level.add(child)
                        seen.add(child)
                
                if found: break
            if found: break
            
            # Move to the next "minute" of divisions
            current_level = next_level

        if found:
            print(minutes)
        else:
            print(-1)