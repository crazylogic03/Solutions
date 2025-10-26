n = int(input())

def pyramid(n, level=1):
    if level > n:
        return
    pyramid(n, level + 1)
    print(" " * (n - level) + "*" * (2 * level - 1))

pyramid(n)