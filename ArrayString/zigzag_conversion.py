def convert(self, s, numRows):
        r = ""
        numCols = (len(s) // 2) + (numRows // 2)

        if numCols == 0 or numRows == 1:
            for c in s:
                r += c
            return r

        else:
            a = [[" " for j in range(numCols)] for i in range(numRows)]
            c = 0
            i = 0
            j = 0

            while c != len(s):
                if i == 0:
                    while i < numRows and c != len(s):
                        a[i][j] = s[c]
                        c += 1
                        i += 1
                    i -= 1
                else:
                    i -= 1
                    j += 1
                    if i == 0:
                        continue
                    a[i][j] = s[c]
                    c += 1

            for i in range(numRows):
                for j in range(numCols):
                    if a[i][j] != " ":
                        r += a[i][j]
            return r
