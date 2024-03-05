def reverseWords(self, s):
    s = s.strip()
    s = s.split()
    count = 0

    for x in range(len(s)):
        y = s.pop()
        s.insert(count, y)
        count += 1

    s = ' '.join(s)
    return s