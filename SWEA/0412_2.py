#1284. 수도요금 경쟁

tc= int(input())
for t in range(1,tc+1):
    p,q,r,s,w=map(int,input().split())
    answer=0

    answer=w*p # a사

    if w<=r:
        answer=min(answer,q)
    else:
        answer=min(answer,q+(w-r)*s)

    print(f'#{t} {answer}')

