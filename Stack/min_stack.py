class MinStack(object):
    def __init__(self):
        self.stack = []
        self.sort_stack = []

    def push(self, val):
        self.stack.append(val)
        self.sort_stack.append(val)
        self.sort_stack.sort()

    def pop(self):
        self.sort_stack.pop(self.sort_stack.index(self.stack.pop()))

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.sort_stack[0]
