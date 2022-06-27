#14500 테트로미노 (다시풀기)
# ㅜ모양을 제외한 4개 모양들은 블록4개로 상하좌우 섞어 만들수있는 모든 모양임. (1234 의 모든 수열을 dfs로 구하듯) 
# ㅜ모양은 다른 모양과 달리 2번째 블록을 선택하고 다음 블록 선택시 새로운 블록(ny,nx)에서도 dfs호출하고 기존 블록(y,x)에서도 dfs호출해야함(이게 맞게 이해한건진 모르겠음..)

n,m=map(int,input().split()) # 세로 X 가로
arr= []
for i in range(n):
    arr.append(list(map(int,input().split())))
visited=[ [0]*m for i in range(n)]

dy=[-1,0,1,0]
dx=[0,1,0,-1]
answer=0
max_val = max(map(max,arr)) # 2차원 배열 arr중에 제일 큰 값

def dfs(y,x,block_cnt,total):
    global answer

    if answer>=total+max_val*(4-block_cnt): # 현재값 + 나머지 블록이 모두 최댓값이더라도 기존의 answer값이 더크면 
        return  # 그냥 리턴
    if block_cnt==4: # 4개의 블록을 모두 count했으면
        answer=max(answer,total)
        return
    
    else:           
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]

            if 0<=ny<n and 0<=nx<m and visited[ny][nx]==0:
                if block_cnt==2: # ㅗ모양, 2개의 블록을 카운트했다면
                    visited[ny][nx]=1
                    dfs(y,x,block_cnt+1,total+arr[ny][nx]) # 기존의 위치에서 재귀호출
                    visited[ny][nx]=0
                
                visited[ny][nx]=1
                dfs(ny,nx,block_cnt+1,total+arr[ny][nx])
                visited[ny][nx]=0

for y in range(n):
    for x in range(m):
        visited[y][x]=1
        dfs(y,x,1,arr[y][x])
        visited[y][x]=0
print(answer)

            
