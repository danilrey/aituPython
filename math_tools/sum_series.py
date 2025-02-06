def sum_series(n: int):
    total = 0
    for i in range(n):
        total += 2 ** i
    return total