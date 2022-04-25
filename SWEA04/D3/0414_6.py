# 2805. 농작물 수확하기
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[ list(map(int,input())) for i in range(n)]
    center=n//2
    answer=0

    for i in range(n):
        if i<=n//2:
            answer+=sum(arr[i][center-i:center+i+1])
        else:
            answer+=sum(arr[i][i-center:n-(i-center)])
    
    print(f'#{t} {answer}')
