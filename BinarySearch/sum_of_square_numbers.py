def judgeSquareSum(self, c):
    left = 0
    right = int(c ** 0.5)
    
    while left <= right:
        mid = (left * left) + (right * right)
        if mid < c:
            left += 1
        elif mid > c:
            right -= 1
        else:
            return True
    return False
  
