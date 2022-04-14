#3314. 보충학습과 평균

tc=int(input())
for t in range(1,tc+1):
    score=map(int,input().split())
    sum=0
    for i in score:
        if i<40:
            sum+=40
        else:
            sum+=i
    
    print(f'#{t} {sum//5}')