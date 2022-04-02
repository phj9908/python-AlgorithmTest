# n과m(12) : 오름차순 출력+같은수 출력 가능

n,m=map(int,input().split())
num_arr=sorted(list(map(int,input().split())
))
s=[]

def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    remember_me=0
    for i in num_arr[start:]:
        if remember_me==i:
            continue
        s.append(i)
        remember_me=i
        dfs(num_arr.index(i))
        s.pop()
dfs(0)