# n과m(10):이전 조건+오름차순 수열

n,m=map(int,input().split())
num_arr=sorted(list(map(int,input().split())))
s=[]
visited=[False for _ in range(n)]

def dfs(start):
    if len(s)==m:
        print(*s)
        return
    
    remember_me=0
    for i in range(start,n):
        if visited[i] or remember_me==num_arr[i]:
            continue
        s.append(num_arr[i])
        remember_me=num_arr[i]
        visited[i]=True
        dfs(i)
        s.pop()
        visited[i]=False
dfs(0)
