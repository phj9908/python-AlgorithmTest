#12221. 구구단2
tc=int(input())
for t in range(1,tc+1):
    n,m=map(int,input().split())

    if n>9 or m>9:
        answer=-1
    else:
        answer=n*m
    print(f'#{t} {answer}')