# n과m(4) : 이전 조건+ 오름차순

n,m = map(int,input().split())
s=[]

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)