#1715 카드정렬하기( 파일 합치기3와 동일 )
import heapq

n=int(input())
arr=[ int(input()) for i in range(n)]
heapq.heapify(arr)
sum=0
while len(arr)>=2:
    num1=heapq.heappop(arr)
    num2=heapq.heappop(arr)
    sum+=num1+num2
    heapq.heappush(arr,num1+num2)
print(sum)