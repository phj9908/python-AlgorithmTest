# 이중 우선순위 큐
# heapq.nlargest(n,iterable)
# :데이터 집합(iterable)에서 n개의 가장 큰 요소로 구성된 리스트를 반환
 
import heapq

def solution(operation):
    answer=[]

    for oper in operation:
        oper=oper.split()
        if oper[0]=='I':
            heapq.heappush(answer,int(oper[1]))
        elif len(answer)>0 and oper[0]=='D':
            if oper[1]=='-1':
                heapq.heappop(answer)
            else: # 최댓값 pop 할 때!
                answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                # answer.index(heapq.nlargest(1,answer)가 리스트로 반환하기에 [0]로 인덱스 지정 해주기
    if len(answer)==0:
        return [0,0]
    else: # 명령어 실행후, 남은것들중 [가장 큰 원소, 가장 작은 원소 ]
        return [answer.pop(answer.index(heapq.nlargest(1,answer)[0])),answer.pop(answer.index(heapq.nsmallest(1,answer)[0]))]
