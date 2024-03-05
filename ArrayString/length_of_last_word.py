def lengthOfLastWord(self, s):
    s = s.strip()
    if " " not in s:
        return len(s)
    else:
        index = len(s) - 1
        while s[index] != " ":
            index -= 1
        return len(s) - 1 - index