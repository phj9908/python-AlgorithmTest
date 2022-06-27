# 디스크 컨트롤러
# 총 대기시간 최소로 만들기>> 작업의 소요시간이 작은순으로 처리
# 작업의 소요시간 기준으로 최소힙 만들기. 그러므로 jobs의 원소 앞뒤를 바꾸기 [작업의 소요시간, 작업이 요청되는 시점]
# 현재시점에서 처리가능한 작업인가? 작업의 요청시간이 바로이전에 완료한 작업의 시작시간보다 크고 현재 시점보다 작거나 같아야 한다.

# 현재 처리할수 있는 작업이 없을때
# 남아있는 작업들의 요청시간이 아직 오지않은 것이기에 현재 시점을 하나 올려줌

import heapq

def solution(jobs):
    
    answer,now,i = 0,0,0
    start =-1
    heap=[]

    while i<len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap,[j[1],j[0]]) # 작업의 소요시간 기준으로(맨 앞 인덱스에 두기) 최소힙 만들기 , 맨 처음엔 작업 요청시간이 0인 job만 heappush
        if len(heap)>0:
            curr=heapq.heappop(heap)
            start=now
            now+=curr[0] # 작업의 소요시간
            answer+=(now-curr[1]) #now-작업의 요청시점
            i+=1
        else:   # len(heap)==0, 현재 처리할수 있는 작업이 없을때 
            now+=1

    return int(answer/len(jobs))