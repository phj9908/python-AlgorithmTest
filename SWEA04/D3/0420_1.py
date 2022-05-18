# n-queen(dfs,백트래킹 활용)다시 풀기!!
# 아레 그림과 같이 코드보기
# https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-9663-N-Queen-%ED%8C%8C%EC%9D%B4%EC%8D%AC 그림참고!!!

def dfs(arr,n,row):
    cnt=0

    if n==row:
        return 1

    for col in range(n): # 가로로 한번만 진행
        arr[row]=col

        for x in range(row):
            if arr[x] == arr[row]: # 세로로 겹치면 안됨
                break
            if abs(arr[row]-arr[x])==row-x: # 대각선으로 겹치면 안됨
                break
        else: # break로 빠져나간적 없다면 = 이 행에 퀸을 둘 수 있다면
            cnt+=dfs(arr,n,row+1) # 다음 퀸 찾으러 go
    return cnt

tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[0]*n

    print(dfs(arr,n,0))