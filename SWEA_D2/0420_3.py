# 4299. 태혁이의 사랑은 타이밍
tc=int(input())
for t in range(1,tc+1):
    d,h,m=map(int,input().split())
    answer=0
    if d<11 or (d==11 and h<11) or (d==1 and h==11 and m<11):
        answer=-1
    else:
        d=(d-11)*24*60
        h=(h-11)*60
        m=(m-11)

        answer=d+h+m

    print(f'#{t} {answer}')