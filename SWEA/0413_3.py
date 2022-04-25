# 10505.소득 불균형
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    people=list(map(int,input().split()))

    aver=sum(people)/n
    cnt=0
    for p in people:
        if p<=aver:
            cnt+=1
    print(f'{t} {cnt}')