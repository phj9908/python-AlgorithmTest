# 15650 n과m(2) : 이전 조건+ 고른 수열은 오름차순이어야 함
n,m = map(int,input().split())
s=[]
 
def dfs(start):
    if len(s)==m:
        print(*s)
        return
    
    for i in range(start,n+1):
        if i in s:
            continue
        s.append(i)
        dfs(i)
        s.pop()    
dfs(1)