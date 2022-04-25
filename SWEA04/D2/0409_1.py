# 1979 어디에 단어가 들어갈 수 있을 까 (다시 풀어보기)
tc= int(input())
for t in range(1,tc+1):
    n,k=map(int,input().split())
    arr=[]
    answer=0

    for _ in range(n):
        arr.append(list(map(int,input().split())))
    
    for i in range(n):
        
        cnt=0
        for j in range(n):
            if arr[i][j]==1:
                cnt+=1
            if arr[i][j]==1 or j==n-1: # j==n-1 : 0이든 1이든 벽에 도달 했을 때
                if cnt==k:
                    answer+=1
                cnt=0
        
        cnt=0
        for j in range(n):
            if arr[j][i]==1:
                cnt+=1
            if arr[j][i]==0 or j==n-1:
                if cnt==k:
                    answer+=1
                cnt=0

    print(f'#{t} {answer}')

# # 다른풀이( 가벽을 세워서 0과1로 바뀌는 횟수 체크)

# n,k=map(int,input().split())
# arr=[]
# answer=0

# for _ in range(n):
#     arr.append([0]+list(map(int,input().split()))+[0])

# for i in range(n):

#     cnt=0
#     for j in range(n):
#         if arr[i][j]==0:
#             if arr[i][j]!=arr[i][j+1]: # 0다음 1
#                 cnt+=1
#         else:
#             if arr[i][j]==arr[i][j+1]: # 1다음 1
#                 cnt+1
#             else: # 1다음 0
#                 if cnt==k:
#                     answer+=1
#                 cnt=0
    
#     cnt=0
#     for j in range(n):
#         if arr[j][i]==0:
#             if arr[j][i]!=arr[j+1][i]:
#                 cnt+=1
#         else:
#             if arr[j][i]==arr[j+1][i]:
#                 cnt+=1
#             else:
#                 if cnt==k:
#                     answer+=1
#                 cnt=0