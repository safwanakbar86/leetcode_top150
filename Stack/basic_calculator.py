#INCOMPLETE

def basic_calc(s):
    answer, index = basic_calc_recursive(s, ['$'])
    return answer

def basic_calc_recursive(s, stack):
    i = 0
    answer = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue
        elif stack[-1] == '+':
            if s[i] == '(':
                temp, index = basic_calc_recursive(s[i+1:], ['$', '('])
                answer += temp
                i += index
            else:
                answer += int(s[i])
                i += 1
            stack.pop()
        elif stack[-1] == '-':
            if s[i] == '(':
                temp, index = basic_calc_recursive(s[i+1:], ['$', '('])
                answer -= temp
                i += index
            else:
                answer -= int(s[i])
                i += 1
            stack.pop()
        elif s[i] == '(':
            temp, index = basic_calc_recursive(s[i+1:], ['$', '('])
            answer += temp
            i += index
        elif s[i] == ')':
            stack.pop()
            return answer, i+2
        else:
            if s[i] != '+' and s[i] != '-':
                answer += int(s[i])
            else:
                stack.append(s[i])
            i += 1
    return answer, 0

s = "(1+(4+5+2)-3)+(6+8)"
s = s.strip()
answer = basic_calc(s)
print(answer)
