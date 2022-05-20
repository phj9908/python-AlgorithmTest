# n과 m(9) # 중복된 수 포함 한 n개의 수들 중에 m개 수열 만들기
# 이때까진 입력되는 수중에 중복되는 수가 없었기에  if i not in s 조건문만 있으면 됐지만
# 입력되는 수에 중복된 수가 있으면 인덱스로 방문 유무 파악을 하고 >> visited[]
# remember_me 변수로 중복되는 수열 방지
# https://alphatechnic.tistory.com/27 참고하면 좋음

n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
s=[]
visited=[False]*n

def dfs():

    if len(s)==m:
        print(*s)
        return 

    remember_me=0   # 전역변수로하면 안됨(디버깅하면 이해됨)
    for i in range(len(arr)):
        if visited[i]==0 and arr[i]!=remember_me: # remember_me로 동일한 값의 원소를 판별하고, i not in s 조건문 역할도 함
            s.append(arr[i])
            visited[i]=True
            remember_me=arr[i]
            dfs()
            visited[i]=False
            s.pop()
dfs()