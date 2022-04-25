# 11736. 평범한 숫자
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=list(map(int,input().split()))
    answer=0

    for i in range(1,len(arr)-1):
        if (arr[i]>arr[i-1] and arr[i]<arr[i+1]) or (arr[i]<arr[i-1] and arr[i]>arr[i+1]):
            answer+=1
    print(f'#{t} {answer}')