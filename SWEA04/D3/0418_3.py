# 5603. [Professional] 건초더미 : 1 2 7 10 -> 5 5 5 5 로 바꾸는 횟수
# 결과값 5는 그냥 평균값이었다..

tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=sorted([int(input()) for i in range(n)])
    average=sum(arr)//len(arr)
    answer=0

    for i in range(len(arr)):
        if average-arr[i]>0:
            answer+=average-arr[i]
    print(f'#{t} {answer}')
    