# 기능 개발
import math


def solution(progresses, speeds):

    answer = []
    front=0
    progresses=[math.ceil((100-a)/b) for a,b in zip(progresses,speeds)]# 소수점 무조건 올림

    for i in range(len(progresses)):
        if progresses[i] > progresses[front]:
            answer.append(i-front)
            front=i
    
    answer.append(len(progresses)-front)
        
    return answer