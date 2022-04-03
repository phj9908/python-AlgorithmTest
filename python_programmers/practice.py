def solution(priorities,location):
    from collections import deque
    answer=0

    stack=deque([(v,i) for i,v in enumerate(priorities)])

    while stack:
        item=stack.popleft()
        if stack and item[0]<max(stack)[0]:
            stack.append(item)
        else:
            answer+=1
            if item[1]==location:
                break
    return answer
    

    


