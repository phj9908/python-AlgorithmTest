# 14178. 1차원 정원(다시 풀어보기)

tc=int(input())
for t in range(1,tc+1):
    n,d=map(int,input().split())
    answer=0
    one=d*2+1 # 분무기하나로 물을 줄 수있는 꽅의 개수
    if n%one==0: # 모든 꽃에게 물을 줄 수 있음
        answer=n//one # 필요한 분무기 개수
    else: # 남는 꽃이 있다면 
        answer=n//one+1  # 하나 추가하면 됨

    print(f'#{t} {answer}')
