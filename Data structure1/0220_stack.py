import sys

n = int(sys.stdin.readline())
stack=[]

for _ in range(n):
    str = sys.stdin.readline().split()
    word = str[0]
    if word == 'push':
        stack.append(str[1]) # push 1 입력했으면 1만 할당
    elif word == 'pop' : 
        if len(stack)!=0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif word == 'top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
    elif word == 'size':
        print(len(stack))
    elif word == 'empty':
        if len(stack) == 0:
            print(1)
        else :
            print(0)


                    