# 위장 : 옷의 종류(key)와 옷 이름(value)를 주고, 섞어입는 경우의 수

def solution(clothes):
    
    table={}
    for v,k in clothes:
        if k in table.keys():
            table[k].append(v)
        else:
            table[k]=[v] # 같은 key의 다른 value가 들어올 수 있기에 리스트안에 할당한 형태여야 함!!
            
    answer=1    
    for v in table.values():
        answer *= len(v)+1 # 옷의 갯수+ 안입는 경우
        # 예를 들어 상의(key)에 존재하는 옷(value)이 2개, 하의에 존재하는 옷이3개면 총 입을수 있는 경우의 수는 2*3 이기에

    return answer-1 # 최소 한개의 의상은 입기에 -1해주기

# # 다른 풀이(Counter,reduce이용)
# Counter() : 'hello' => {'h':1,'e':1,'l':2,'o':1}
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1 # x*(y+1)값을 누적한 뒤 반환, x=cnt.values()고 y=1
#     return answer