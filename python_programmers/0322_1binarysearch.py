# 입국 심사
# n명의 최소 입국심사 시간 도출

def solution(n,times):
    left=1
    right=max(times)*n # 가장 오래걸리는 심사관이 모두 심사할 때
    answer=0

    while left<=right:
        people=0
        mid=(left+right)//2

        for t in times:
            people+= mid//t

            if people>=n: # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할수 있다면 
                break     # 반복문 나가기
        
        if people<n:
            left=mid+1
        else:
            answer=mid
            right=mid-1

    return answer