from collections import deque
import sys

queue=deque()
n = int(sys.stdin.readline())
for _ in range(n):
    str = sys.stdin.readline().split()
    word = str[0]
    if word == 'push':
        queue.append(str[1])
    elif word == 'pop':
        if queue:
            print(queue[0])
            queue.popleft() # 제일 앞을 제거
        else :
            print(-1)
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        if queue:
            print(0)
        else :
            print(1)
    elif word == 'front':
        if queue:
            print(queue[0])
        else :
            print(-1)
    elif word == 'back':
        if queue:
            print(queue[-1])
        else :
            print(-1)


    