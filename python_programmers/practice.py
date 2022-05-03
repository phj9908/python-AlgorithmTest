
from itertools import permutations
from unicodedata import numeric

# def check(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True


# def solution(numbers):
#     answer=[]
#     for i in range(1,len(numbers)+1):
#         per=list(permutations(numbers,i))

#         for p in list(set(per)):
#             p=''.join(p) # ['1','2'] => '12'
#             if check(int(p)):
#                 answer.append(int(p))
    
#     return len(set(answer))

def solution(numbers):
    a=set()
    for i in range(1,len(numbers)+1):
        a|=list(map(int,map(''.join,permutations(numbers,i))))
    a-=set(range(0,2))
    for i in range(2,int(max(a)**0.5)+1):
        a-=set(range(2*i,max(a),i))
    return len(a)

    