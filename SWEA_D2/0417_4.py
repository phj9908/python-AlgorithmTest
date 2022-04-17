# 5789. 현주의 상자 바꾸기
tc=int(input())
for t in range(1,tc+1):
    n,q=map(int,input().split())
    arr=[0]*n
    i=1
    while i<=q:
        l,r=map(int,input().split())
        for j in range(l-1,r):
            arr[j]=i
        i+=1
    print(f'#{t}',end=' ');print(*arr)
