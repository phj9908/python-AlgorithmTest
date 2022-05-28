# 10819 차이를 최대로
# 샘플 입력엔 중복되는 수가 없지만 중복되는 수가 들어갈수 있다는 가정이 있는듯. visited=[] 필요

# 백트래킹 사용ver
n= int(input())
num=list(map(int,input().split()))
answer=0
s=[]
visited=[False]*n 

def dfs():
    global answer
    if len(s)==n: # 원소다 채웠으면
        total=0 # 순열의 최댓값 차의 합 저장
        for i in range(n-1):    
            total+=abs(s[i]-s[i+1]) 
        answer=max(answer,total)
        return

    for i in range(n):
        if not visited[i]:   
            visited[i]=True
            s.append(num[i])
            dfs()
            visited[i]=False
            s.pop()
dfs()
print(answer)

# # permutation 사용 ver
# from itertools import permutations

# n= int(in.txt())
# num=list(map(int,in.txt().split()))
# answer=0

# per=permutations(num)

# for i in per:
#     sum=0
#     for j in range(n-1):
#         sum+=abs(i[j]-i[j+1])
#         answer=max(answer,sum)
# print(answer)
    
