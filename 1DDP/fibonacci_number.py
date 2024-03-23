    def fib(self, n):
        if n < 0:
            return 0
        elif n <= 1:
            return n
        else:
            memo = []
            memo.append(0)
            memo.append(1)
            for i in range(2, n+1):
                memo.append(memo[i-1] + memo[i-2])
            return memo[-1]
