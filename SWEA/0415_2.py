# 4466. 최대 성적표 만들기
tc=int(input())
for t in range(1,tc+1):
    n,k =map(int,input().split())
    score=list(map(int,input().split()))

    score=sorted(score,reverse=True)
    answer=sum(score[:k])

    print(f'#{t} {answer}')