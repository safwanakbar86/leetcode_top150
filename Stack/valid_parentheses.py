def isValid(self, s):
    stack = []

    for t in s:
        if stack == []:
            stack.append(t)
        elif stack[-1] == '(' and t == ')':
            stack.pop()
        elif stack[-1] == '[' and t == ']':
            stack.pop()
        elif stack[-1] == '{' and t == '}':
            stack.pop()
        else:
            stack.append(t)

    if stack == []:
        return True
    else:
        return False
