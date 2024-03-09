#INCOMPLETE

def basic_calc(s):
    return basic_calc_recursive(s, [])

def basic_calc_recursive(s, stack):
    answer = 0
    for c in range(len(s)):
        if c == ' ':
            continue
        elif stack[-1] == '+':
            if c == '(':
                answer += basic_calc_recursive(s[c+1:], ['('])
            else:
                answer += int(c)
                stack.pop()
        elif stack[-1] == '-':
            if c == '(':
                answer -= basic_calc_recursive(s[c+1:], ['('])
            else:
                answer -= int(c)
                stack.pop()
        elif c == '(':
            answer += basic_calc_recursive(s[c+1:], ['('])
        elif c == ')':
            stack.pop()
            return answer
        else:
            if c != '+' or c != '-':
                answer += c
            else:
                stack.append(c)
    return answer

s = "   1 + 1 "
#s = "  2-1 + 2 "
#s = "(1+(4+5+2)-3)+(6+8)"
s = s.strip()
answer = basic_calc(s)
print(answer)
