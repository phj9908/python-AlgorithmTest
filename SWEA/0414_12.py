# 1209. [S/W 문제해결 기본] 2일차 - Sum
import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    #tc=int(input())
    arr=[ list(map(int,sys.stdin.readline().split())) for i in range(100)]

    answer=0
    for i in range(100):
        answer=max(answer,sum(arr[i]))

        s=0
        for j in range(100):
            s+=arr[j][i]
        answer=max(answer,s)

    sum_a=0
    sum_b=0
    for i in range(100):
        for j in range(100):
            if i==j:
                sum_a+=arr[i][j]
            if i==j-99:
                sum_b+=arr[i][j]
    answer=max(answer,sum_a,sum_b)

    print(f'#{t} {answer}')


