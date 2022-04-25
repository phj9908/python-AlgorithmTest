# 5948. 새샘이의 7-3-5 게임
from itertools import combinations

tc=int(input())
for t in range(1,tc+1):
    arr= list(map(int,input().split()))
    combination=list(combinations(arr,3))
    answer=[]
    for i in combination:
        answer.append(sum(i))
    answer=list(set(answer))
    answer=sorted(answer,reverse=True)
    print(f'#{t} {answer[4]}')
