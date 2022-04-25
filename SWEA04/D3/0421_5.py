# 10726. 이진수 표현
tc=int(input())
for t in range(1,tc+1):
    n,m = map(int,input().split())
    m=bin(m)[2:]
    #print(m[-n:])
    if m[-n:]=='1'*n:
        answer='ON'
    else:
        answer='OFF'

    print(f'#{t} {answer}')