# 10974 모든 순열 : 1부터 N까지 모든 순열 사전순으로 출력
# 백트래킹 이용(dfs)

n=int(input())
num=[]

def dfs():
    if len(num)==n:
        print(*num)
        return
    
    for i in range(1,n+1):
        if i not in num:
            num.append(i)
            dfs()
            num.pop()

dfs()



# 다른 풀이
# from itertools import permutations

# n=int(input())
# num=[i for i in range(1,n+1)]

# for p in permutations(num):
#     print(*p)

