#  카드정렬하기 (다시 풀어보기)
#  우선순위 큐(힙) 활용

import heapq

n=int(input())
heap=[]
for i in range(n):
    heapq.heappush(heap,int(input()))
answer=0

while len(heapq)>1:
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)

    answer+=one+two
    heapq.heappush(answer)

print(answer)
