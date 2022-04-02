# 15649 N과M (1) : 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 모두 출력

# DFS를 기반한 백트래킹 구현 ver. (N까지의 숫자를 트리로 구성했다고 생각!)
n,m = map(int,input().split())
s=[]

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s))) # ''.join()은 str만 처리함
        return
    for i in range(1,n+1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()


# permutataion 이용한 ver.
# from itertools import permutations

# n,m = map(int,input().split())
# per_list=[ i for i in range(1,n+1)] # [1,2,3,4]
# per_list=list(permutations(per_list,m))
# for i in per_list:
#     print(*list(i))