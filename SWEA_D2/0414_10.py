# 5431. 민석이의 과제 체크하기
tc=int(input())
for t in range(1,tc+1):
    n, k=map(int,input().split())
    arr=set([ i for i in range(1,n+1)])
    k_arr=set(map(int,input().split()))
    arr-=k_arr

    print(f'#{t}',end=' ');print(*arr)
    