def mySqrt(self, x):
    c = 0
    n = 1
    
    while n * n <= x:
        n += 1
        c += 1
    
    return c
