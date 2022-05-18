# 19598 최소 회의실 개수( 다시풀기 )
# cf)1931번 회의실배정 문제는 1개!!!의 회의실에서 가능한 최대 회의갯수 도출 : 끝나는 시간을 기준으로 오름차순 정렬
# 이 문제에선 끝나는 시간을 기준으로 오름차순을 하면 안되는 이유 https://hillier.tistory.com/115
import heapq

n=int(input())
arr=[ list(map(int,input().split())) for i in range(n)]
arr=sorted(arr,key=lambda x:x[0])
heap=[]
for s,e in arr:
    if heap and s>=heap[0]: # 이전 종료시간보다 이번 시작시간이 늦다면
        heapq.heappop(heap) # 이전 종료시간 pop
    heapq.heappush(heap,e) # 새로운 회의실 추가
print(len(heap))