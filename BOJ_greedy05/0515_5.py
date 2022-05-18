#11000 강의실 배정
# 19598 최소 회의실 갯수와 동일
import heapq,sys
input = sys.stdin.readline

n=int(input())
arr=[ list(map(int,input().split())) for i in range(n)]
arr=sorted(arr,key=lambda x:x[0])
heap=[]
for s,e in arr:
    if heap and heap[0]<=s:
        heapq.heappop(heap)
    heapq.heappush(heap,e)
print(len(heap))