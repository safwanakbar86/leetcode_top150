def mySqrt(self, x):
    n = 0
    while n * n <= x:
        n += 1
    return n - 1
