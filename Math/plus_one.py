def plusOne(self, digits):
    n = 0
    x = 1
    for i in range(len(digits) - 1, -1, -1):
        n += digits[i] * x
        x *= 10
    n += 1
    
    temp = []
    i = -1
    while n > 0:
        temp.insert(i, n % 10)
        n /= 10
        i -= 1
    return temp