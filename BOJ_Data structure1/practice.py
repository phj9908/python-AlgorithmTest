import sys

n=int(input())
arr=[ list(map(int,input().split())) for i in range(n)]
min_value=sys.maxsize

def dfs(start,curr,value,s):
    global min_value
    if len(s)==n:
        if arr[curr][start]!=0:
            min_value=min(min_value,value+arr[curr][start])
        return
    
    for i in range(n):
        if arr[curr][i]!=0 and i not in s and value<min_value:
            s.append(i)
            dfs(start,i,value+arr[curr][i],s)
            s.pop()
for i in range(n):
    dfs(i,i,0,[i])
print(min_value)