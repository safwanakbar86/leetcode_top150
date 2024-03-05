def isPalindrome(self, s):
    if not s.islower():
        s = s.lower()

    r = ""
    for x in s:
        if (ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 48 and ord(x) <= 57):
            r += x
    s = r
    
    if s == s[::-1]:
        return True
    else:
        return False
