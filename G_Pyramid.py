n = int(input())

def pyramid(n, level=1):
    if level > n:
        return
    print(" " * (n - level) + "*" * (2 * level - 1))
    pyramid(n, level + 1)

pyramid(n)