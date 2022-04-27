# 3975. 승률 비교하기
# 100000개 테케라서 시간절약을 위해 answer에 모아뒀다가 한꺼번에 출력
tc=int(input())
answer=[]
for t in range(1,tc+1):
    a,b,c,d=map(int,input().split())
    alice=a/b
    bob=c/d
    if alice>bob:
        answer.append('ALICE')
    elif alice<bob:
        answer.append('BOB')
    else:
        answer.append('DRAW')

for t in range(1,tc+1):
    print(f'#{t}',end=' ')
    print(answer[t-1])

