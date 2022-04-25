# 간단한 소인수 분해

tc = int(input())
arr=[2,3,5,7,11]
for t in range(1,tc+1):
    num=int(input())
    n=num
    answer=[0]*len(arr)
    for i in arr:
        ans=0
        while n%i==0:
            n//=i
            ans+=1
        answer[arr.index(i)]=ans
    print(f'#{t}',end=' ');print(*answer)