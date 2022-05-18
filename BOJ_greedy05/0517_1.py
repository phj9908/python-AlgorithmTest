# 13975 파일합치기3 ( 예제와는 달리..우선순위큐!!, 다시풀기)
import heapq

for t in range(int(input())):
    k=int(input())
    arr=list(map(int,input().split()))
    heapq.heapify(arr)
    sum=0

    while len(arr)>=2:
        num1=heapq.heappop(arr)
        num2=heapq.heappop(arr)
        sum+=num1+num2 # 비용 누적합
        heapq.heappush(arr,num1+num2) # 각 비용
    print(sum)