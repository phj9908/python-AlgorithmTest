#11053 : 가장 긴 증가하는 부분 수열 4 2 5 10 11 8 => 4 5 10 11
# 유튜브 이코테 다이나믹 프로그래밍- 50분 쯤에 병사문제 참고
n=int(input())
arr=list(map(int,input().split())) # 4 2 5
dp=[1]*(n+1) # 아무리 길이가 짧아도 1이 되기에 1로 초기화

for i in range(1,len(arr)): #dp[0]은 당연히 1이니까 [1]부터 시작
    for j in range(i):
        if arr[j]<arr[i]: # 오름차순 정렬이니까 arr[j]=4이고 arr[i]=2일 때이면 실행 안되도록
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))