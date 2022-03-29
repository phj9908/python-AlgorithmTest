# 더 맵게

# 파이썬 Heapq 라이브러리 이용!
# import heapq
# heapq.heapify(리스트) # 아무렇게나 정렬된 리스트로부터 최소힙 구성
# m = heapq.heappop(리스트)  # 최소값 삭제(반환)
# heapq.heappush(리스트,x) # x를 삽입

import heapq

def solution(sccoville,K):
    answer=0
    heapq.heapify(sccoville)

    while True:
        min1=heapq.heappop(sccoville)
        if min1>=K: # = scoville[0] >= K
            break
        elif len(sccoville)==0: # heapq는 len()를 적용할수없음. 리스트 자체의 길이를 검사해야함
            answer=-1
            break
        else:
            min2=heapq.heappop(sccoville)
            new_min=min1+min*2
            heapq.heappush(sccoville,new_min)
            answer+=1
    return answer