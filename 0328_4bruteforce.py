# 소수찾기
from itertools import permutations
import math
'''
ㅇㅇㅇㅇㅇㅇㅇㅇㅇㄹㅇㅁㄻㄹㅇㅁㄻㄹㄴㅁㄻㅇㄴ
'''
def check(number):
    if number<2:
       return False
    k=math.sqrt(number)
    for i in range(2,int(k)+1):
        if number%i==0:
            return False
    return True

def solution(numbers):
    answer =[]
    #print(list(numbers))
    for i in range(1,len(numbers)+1): # 자리수별 가능한 조합들 도출
        res=list(map(''.join,permutations(list(numbers),i))) # list('abc')=['a','b','c']
        #print(res)
        for j in list(set(res)):
            if check(int(j)):
                answer.append(int(j))
    return len(set(answer)) # 다른 자리수끼리 겹칠수도 있기에 1과 01 처럼

# 다른풀이 (set 활용)

# def solution(n):
#     a=set()
#     for i in range(len(n)):
#         a |= set(map(int,map(''.join,permutaions(list(n),i+1)))) # a = a|set(...) : 합집합
#     a -=set(range(0,2)) # a집합에서 set(range(0,2)) 제거
#     for i in range(2,int(max(a)**0.5)+1):
#         a -=set(range(i*2,max(a)+1,i))
#     return len(a)