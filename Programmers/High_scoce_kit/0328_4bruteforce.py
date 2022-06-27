# 소수찾기

from itertools import permutations

def check(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def solution(numbers):
    answer=[]
    for i in range(1,len(numbers)+1):
        per=list(permutations(numbers,i))

        for p in list(set(per)):
            p=''.join(p) # ['1','2'] => '12'
            if check(int(p)):
                answer.append(int(p))
    
    return len(set(answer)) # 다른 자리수끼리 겹칠수도 있기에 1과 01 처럼

# 다른풀이 (set 활용)
# a = a|set(...) : 합집합
#
# def solution(n):
#     a=set()
#     for i in range(len(n)):
#         a |= set(map(int,map(''.join,permutaions(list(n),i+1)))) # 찢어진 종이들로 만들수 있는 모든 수
#     
#     #소수가 아닌 수 제거
#     a -=set(range(0,2)) # a집합에서 set(range(0,2)) 제거
#     for i in range(2,int(max(a)**0.5)+1):
#         a -=set(range(i*2,max(a)+1,i))
#     return len(a)