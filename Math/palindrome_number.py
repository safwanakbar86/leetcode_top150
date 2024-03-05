def isPalindrome(self, x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        y = x
        z = 1
        while y != 0:
            y = int(y / 10)
            z *= 10
        z /= 10

        y = x
        i = 0
        while y != 0:
            i = i + ((y % 10) * z)
            y = int(y / 10)
            z = int(z / 10)
    
        if i == x:
            return True
        else:
            return False
