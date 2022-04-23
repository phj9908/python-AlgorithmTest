# 실패율, 다시풀어보기

def solution(N, stages):
    answer=[]
    whole=len(stages)

    for i in range(1,N+1):
        if whole<=0: # 분모가 0이 되면 
            fail=0
        else:
            fail=stages.count(i)/whole
        answer.append((i,fail))
        whole-=stages.count(i)
        
    answer=sorted(answer,key=lambda x:x[1],reverse=True)
    answer=[ i[0] for i in answer] # answer의 첫번째 인덱스들 리스트화
        
    return answer