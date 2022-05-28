# 1206. [S/W 문제해결 기본] 1일차 - View
import sys
sys.stdin=open('in.txt.txt')

for t in range(1,11):
    length=100
    #length=int(in.txt())

    arr=list(map(int,sys.stdin.readline().split()))
    answer=0

    for i in range(2,length-2):
        t=0
        while 1:
            if arr[i]-t>arr[i+1] and arr[i]-t>arr[i+2] and arr[i]-t>arr[i-1] and arr[i]-t>arr[i-2] :
                answer+=1
                t+=1
            else:
                break

    print(f'#{t} {answer}')