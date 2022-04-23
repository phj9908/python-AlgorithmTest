# 3233. 정삼각형 분할 놀이
tc=int(input())
for t in range(1,tc+1):
    a,b=map(int,input().split())
    answer=(a//b)**2
    print(f'#{t} {answer}')