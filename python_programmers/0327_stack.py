# 프린터
from collections import deque

def solution(priorities,location):

    arr=[(i,v) for i,v in enumerate(priorities)]
    stack=deque(arr)
    answer=0

    while stack:
        item=stack.popleft()
        if stack and max(stack)[1]>item[1]: # 뒤에 중요도가 더 큰게 있다면 
            stack.append(item) # 맨 뒤에 다시 저장
        else:   # 뒤에 중요도가 더큰게 없다면 그대로 자신을 pop (popleft니까)
            answer+=1   
            if location==item[0]:
                return answer

# 2 1 3 2 에서 location = 0이라하면
# 2 1 3 2
# 1 3 2 2
# 3 2 2 1 -> 여기서부터 else조건문으로 감!! answer+=1
# 2 2 1 -> answer+=1
# 2 1  -> answer+=1 => answer=2
