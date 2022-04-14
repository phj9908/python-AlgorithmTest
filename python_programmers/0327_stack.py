# 프린터
from collections import deque

def solution(priorities, location):
    stack=deque([(value,idx) for idx,value in enumerate(priorities)])
    answer=0

    while stack:
        item=stack.popleft()
        if stack and max(stack)[0] > item[0]: # if stack and 해주는 이유는 popleft()한 뒤 큐가 비어있으면 max(stack)에서 오류 발생하기때문
            stack.append(item)
        else:
            answer+=1
            if location==item[1]:
                return answer
                
solution([1, 1, 9, 1, 1, 1],0)
# 1 1 9 1 1 1
# 1 9 1 1 1 1
# 9 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1
# 1 1 1 
# 1 1