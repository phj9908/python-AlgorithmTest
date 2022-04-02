#14002 : 가장 긴 증가하는 부분 수열4
n=int(input())
arr=list(map(int,input().split())) # 4 2 5
dp=[1]*(n+1) # 아무리 길이가 짧아도 1이 되기에 1로 초기화
res=[]
for i in range(1,len(arr)): #dp[0]은 당연히 1이니까 [1]부터 시작
    for j in range(i):
        if arr[j]<arr[i] : # 오름차순 정렬이니까 arr[j]=4이고 arr[i]=2일 때이면 실행 안되도록
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))

max_num=max(dp)
res=[]
for i in range(len(arr)-1,-1,-1):
    if dp[i]==max_num:
        res.append(arr[i])
        max_num-=1
        if max_num < 1:
            break
res.reverse()
print(*res)