def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack = []
        i = 0
        while i != len(tokens):
            if tokens[i] == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif tokens[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif tokens[i] == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if num1 / num2 < 0:
                    stack.append(math.ceil(num1 / num2))
                else:
                    stack.append(math.floor(num1 / num2))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack.pop()
