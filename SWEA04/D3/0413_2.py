# 12368. 24시간
tc=int(input())
for t in range(1,tc+1):
    a,b=map(int,input().split())
    answer=a+b
    if answer>=24:
        answer%=24
    print(f'{t} {answer}')