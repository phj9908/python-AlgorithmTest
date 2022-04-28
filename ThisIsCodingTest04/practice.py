n,m=map(int,input().split())
arr=[ list(map(int,input().split())) for i in range(n)]
answer=0

def dfs(y,x):
    if x>m-1 or x<0 or y<0 or y<n-1:
        return False
    if arr[y][x]==0:
        arr[y][x]=1

        dfs(y+1,x)
        dfs(y-1,x)
        dfs(y,x+1)
        dfs(y,x-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j):
            answer+=1
print(answer)