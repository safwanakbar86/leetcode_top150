def trailingZeroes(self, n):
    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n-1)
    
    if n == 0:
        return 0
    
    answer = factorial(n)
    answer = str(answer)
    
    c = 0
    for a in range(len(answer) -1, -1, -1):
        if answer[a] == '0':
            c += 1
        else:
            break
    return c
  
