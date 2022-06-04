# 소수만들기
from itertools import combinations

def prime(p):
    for j in range(2,p):
        if p%j==0:
            break
    else:
        return True
    return False

def solution(nums):
    answer = 0
    for p in list(combinations(nums,3)):
        if prime(sum(p)):
            answer+=1

    return answer