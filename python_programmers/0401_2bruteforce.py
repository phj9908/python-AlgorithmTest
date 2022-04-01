# n과m(7)

n,m=map(int,input().split())
num_arr=sorted(list(map(int,input().split())))
s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in num_arr:
        s.append(i)
        dfs()
        s.pop()
dfs()