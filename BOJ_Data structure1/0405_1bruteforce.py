# 10819 차이를 최대로

# 백트래킹 사용ver
n= int(input())
num=list(map(int,input().split()))
answer=0
s=[]
visited=[False]*n # 이미 계산한 숫자를 확인하기 위해

def dfs():
    global answer
    if len(s)==n: # 원소다 채웠으면
        total=0 # 순열의 최댓값 차의 합 저장
        for i in range(n-1):    
            total+=abs(s[i]-s[i+1]) 
        answer=max(answer,total)
        return

    for i in range(n):
        if not visited[i]:  # 아직 계산이 안됐다면
            visited[i]=True
            s.append(num[i])
            dfs()
            visited[i]=False
            s.pop()
dfs()
print(answer)

# # permutation 사용 ver
# from itertools import permutations

# n= int(input())
# num=list(map(int,input().split()))
# answer=0

# per=permutations(num)

# for i in per:
#     sum=0
#     for j in range(n-1):
#         sum+=abs(i[j]-i[j+1])
#         answer=max(answer,sum)
# print(answer)
    
