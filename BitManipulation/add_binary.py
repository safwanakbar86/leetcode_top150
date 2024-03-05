def addBinary(self, a, b):
    def bin_to_dec(s):
        i = -1
        j = 0
        num = 0
        while i != (-1 - len(s)):
            if s[i] == '1':
                num += pow(2, j)
            j += 1
            i -= 1
        return num

    num1 = bin_to_dec(a)
    num2 = bin_to_dec(b)

    ans = num1 + num2
    ans = bin(ans)

    new_ans = ""
    new_ans += ans[2:]
    return new_ans
