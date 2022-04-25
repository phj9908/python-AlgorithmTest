# 지그재그 숫자
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    answer=1
    for i in range(2,n+1):
        if i%2==0:
            answer-=i
        else:
            answer+=i
    print(f'#{t} {answer}')