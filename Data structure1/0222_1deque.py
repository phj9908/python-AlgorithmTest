#10866 덱
from collections import deque
from queue import Empty
import sys

deq=deque()
n= int(sys.stdin.readline())

def push_front(x,deq):
    deq.appendleft(x)
    return deq
def push_back(x,deq):
    deq.append(x)
    return deq
def pop_front(deq):
    if deq :
        print(deq.popleft())
    else :
        print(-1)
def pop_back(deq):
    if deq :
        print(deq.pop())
    else :
        print(-1)
def size(deq):
    print(len(deq))
def empty(deq):
    if deq :
        print(0)
    else :
        print(1)
def front(deq):
    if deq:
        print(deq[0])
    else :
        print(-1)
def back(deq):
    if deq:
        print(deq[-1])
    else :
        print(-1)


str_list={
    'push_front':push_front, # key-value ,value로 함수 매칭
    'push_back':push_back,
    'pop_front':pop_front,
    'pop_back':pop_back,
    'size':size,
    'empty':empty,
    'front':front,
    'back':back
}

for _ in range(n):
    str = sys.stdin.readline().split()
    
    if len(str) ==1 : # push_front, push_back 외 명령어
        str_list[str[0]](deq) 
    else :              # push_front, push_back  
        deq = str_list[str[0]](str[1],deq)
    