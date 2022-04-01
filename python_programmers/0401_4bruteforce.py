# n과 m(9) # 중복된 수 포함 한 n개의 수들 중에 m개 수열 만들기
# https://alphatechnic.tistory.com/27 참고하면 좋음

n,m=map(int,input().split())
num_list=sorted(list(map(int,input().split())))
s=[]
visited=[ False for _ in range(n)] # 중복해서 수열을 출력하지 않도록 ex) (1,1) / if ...in list 는 시간초과되어 visited[]로 체크

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    remember_me=0
    for i in range(n):
        if visited[i] or remember_me == num_list[i]:
            continue
        s.append(num_list[i])
        visited[i]=True
        remember_me=num_list[i] 
        dfs()
        s.pop()
        visited[i]=False
dfs()