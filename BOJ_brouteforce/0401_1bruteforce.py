# n과m(6) : 

n,m= map(int,input().split())
num_arr=sorted(list(map(int,input().split())))
s=[]

def dfs(start):
    if len(s)==m:
        print(*s)
        return
    
    for i in num_arr[start:]:
        if i in s:
            continue
        s.append(i)
        dfs(num_arr.index(i))
        s.pop()
dfs(0)