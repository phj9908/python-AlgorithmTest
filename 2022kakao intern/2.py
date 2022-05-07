from collections import deque

def solution(queue1, queue2):
    answer = -2
    if max(queue1) > (sum(queue1)-max(queue1))+sum(queue2):
        return -1
    elif max(queue2) > (sum(queue2)-max(queue2))+sum(queue1):
        return -1

    length=len(queue1)
    # while 1:
    #     for i in range(length):


    return answer