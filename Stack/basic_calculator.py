def calculate(self, s):
        def basic_calc(s):
            answer, index = basic_calc_recursive(s, ['$'])
            return answer

        def basic_calc_recursive(s, stack):
            i = 0
            answer = 0
            string = ""

            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    continue
                elif stack[-1] == '+':
                    if s[i] == '(':
                        temp, index = basic_calc_recursive(s[i+1:], ['$'])
                        answer += temp
                        i += index
                        stack.pop()
                    elif s[i] == ')':
                        answer += int(string)
                        string = ""
                        stack.pop()
                        return answer, i+2
                    elif s[i] != '+' and s[i] != '-':
                        string += s[i]
                        i += 1
                    else:
                        if string != "":
                            answer += int(string)
                            string = ""
                        stack.pop()
                elif stack[-1] == '-':
                    if s[i] == '(':
                        temp, index = basic_calc_recursive(s[i+1:], ['$'])
                        answer -= temp
                        i += index
                        stack.pop()
                    elif s[i] == ')':
                        answer -= int(string)
                        string = ""
                        stack.pop()
                        return answer, i+2
                    elif s[i] != '+' and s[i] != '-':
                        string += s[i]
                        i += 1
                    else:
                        if string != "":
                            answer -= int(string)
                            string = ""
                        stack.pop()
                elif s[i] == '(':
                    temp, index = basic_calc_recursive(s[i+1:], ['$'])
                    answer += temp
                    i += index
                elif s[i] == ')':
                    if string != "":
                        answer += int(string)
                        string = ""
                    stack.pop()
                    return answer, i+2
                else:
                    if s[i] != '+' and s[i] != '-':
                        string += s[i]
                    else:
                        if string != "":
                            answer += int(string)
                            string = ""
                        stack.append(s[i])
                    i += 1

            if stack[-1] == '+':
                answer += int(string)
                string = ""
                stack.pop()
            elif stack[-1] == '-':
                answer -= int(string)
                string = ""
                stack.pop()
            if answer == 0 and string != "":
                answer = int(string)
            return answer, 0

        s = s.strip()
        answer = basic_calc(s)
        return answer
