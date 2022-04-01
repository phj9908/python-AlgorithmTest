# n과m(11) : 같은수를 골라도 됨 ex) (1,1) 됨

n,m=map(int,input().split())
num_arr=sorted(list(map(int,input().split())
))
s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    remember_me=0
    for i in num_arr:
        if remember_me==i:
            continue
        s.append(i)
        remember_me=i
        dfs()
        s.pop()
dfs()