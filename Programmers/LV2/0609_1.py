# 메뉴 리뉴얼 ( 두 가지 방법으로 풀기 )
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        arr=[]
        for order in orders:
            for combi in combinations(order,c):
                combi=''.join(sorted(combi)) # 사전순 정렬
                arr.append(combi)
        sorted_arr=Counter(arr).most_common()
        for menu,cnt in sorted_arr:
            if cnt>1 and cnt==sorted_arr[0][1]: # 최빈값과 같다면
                answer.append(menu)

    return sorted(answer)


# hash 이용한 다른 방법!!
def solution2(orders, course):
    answer = []
    hash={}
    for c in course:
        for order in orders:
            for combi in combinations(order,c):
                combi=''.join(sorted(combi)) # 사전순 정렬
                if combi in hash.keys():
                    hash[combi]+=1
                else:
                    hash[combi]=1

    max_v=[ 0 for _ in range(len(course))] # hash는 max()함수 사용 불가능하기에
    max_key=[ [] for _ in range(len(course))] # maxdls  value,그 value의 key의 리스트 각각 생성

    for key in hash:
        for i,v in enumerate(course):
            if len(key)==v:
                if hash[key]>max_v[i]:
                    max_v[i]=hash[key]
                    max_key[i]=[key]
                elif hash[key]==max_v[i]:
                    max_key[i].append(key)

    for i,v in enumerate(max_v):
        if v>=2:
            answer.append(max_key[i])

    return sorted(answer)