# 10974 모든 순열 : 1부터 N까지 모든 순열 사전순으로 출력

# '15649 N과M (1) : 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 모두 출력' 와 동일함!!!
# DFS를 기반한 백트래킹 구현/(N까지의 숫자를 트리로 구성했다고 생각!)

n=int(input())
num=[]

def dfs():
    if len(num)==n:
        print(*num)
        return
    
    for i in range(1,n+1):
        if i not in num: # 숫자가 중복되지 않도록함
            num.append(i)
            dfs()
            num.pop()

dfs()



# 다른 풀이
# from itertools import permutations

# n=int(in.txt())
# num=[i for i in range(1,n+1)]

# for p in permutations(num):
#     print(*p)

