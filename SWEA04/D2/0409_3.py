#1966. 숫자를 정렬하자

tc= int(input())
for t in range(1,tc+1):
    n=int(input())
    nums=list(map(int,input().split()))
    nums=sorted(nums)
    
    print(f'#{t}',end=' ');print(*nums)