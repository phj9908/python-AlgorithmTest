# n과m(3) : 중복포함하여 1부터 N까지 자연수 중에서 M개를 고른 수열

n,m = map(int,input().split())
s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()