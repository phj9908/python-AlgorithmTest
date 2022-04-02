# 15654 n과m(5) : n개의 자연수들에서 m개를 고른 수열, 증가하는 순으로 출력

n,m =map(int,input().split())
num_list=sorted(list(map(int,input().split())))

s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in num_list:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()
dfs()