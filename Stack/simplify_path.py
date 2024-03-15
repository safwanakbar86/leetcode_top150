#path = "/home/"
#/home

#path = "/home//foo/"
#/home/foo"

#path = "/../"
#/

#path = "/a/./b/../../c/"
#/c

path = "/a/../../b/../c//.//"
#/c

path = "/a//b////c/d//././/.."
#/a/b/c

stack = ['$']
r = "/"
p = 1

while p < len(path):
    if path[p] == '.' and path[p - 1] == '.' and stack[-1] != '$':
        if stack[-1] == '/':
            stack.pop()
            stack.pop()
        else:
            stack.pop()
    elif path[p] == '/' and path[p - 1] != '.' and path[p - 1] != path[p]:
        stack.append('/')
    elif path[p] != '/' and path[p] != '.':
        stack.append(path[p])
    p += 1

if stack[-1] == '/':
    stack.pop()
    
for s in range(1, len(stack)):
    r += stack[s]
print(r)
