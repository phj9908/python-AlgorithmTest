# 음료수 얼려먹기(다시 풀어보기)

# dfs
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
answer=0

def dfs(y,x):
    if x>=m or x<0 or y<0 or y>=n:
        return False
    if arr[y][x]==0:
        arr[y][x]=1 # 방문 처리

        # 해당 좌표의 상하좌우 좌표에 방문처리
        dfs(y-1,x) 
        dfs(y+1,x) 
        dfs(y,x-1) 
        dfs(y,x+1) 
        return True
    return False

# 각 좌표마다 dfs 실행
for i in range(n): 
    for j in range(m):
        if dfs(i,j): # 현재 좌표와 연결된 좌표 탐색 
            answer+=1
print(answer)