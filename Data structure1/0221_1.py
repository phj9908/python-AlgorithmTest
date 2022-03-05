#10845 큐
# -스택과 달리 선입선출 구조.
# -스택의 top:bottom / 큐의 front : back (front:[0]/ back:[-1])
# -스택은 append. 차곡차곡 쌓임
# -*큐는 insert(0,원소). [0]의 자리에 차곡차곡 쌓임. 맨처음 넣은게 [-1]자리에 가있음
# -스택은 pop(),맨뒤 제거/ 큐는 pop(0),맨 앞 제거

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


    