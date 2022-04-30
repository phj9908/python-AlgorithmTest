# 3304. 최장 공통 부분 수열 (다시 풀기)
# https://deok2kim.tistory.com/143 

for t in range(1,int(input())+1):
    #words=list(input())
    a,b=input().split()
    answer=0
    a=' '+a
    b=' '+b
    
    dp=[ [0]*len(a) for _ in range(len(b))]

    for i in range(1,len(b)):
        for j in range(1,len(a)):
            if b[i]==a[j]:          # 같을 때
                dp[i][j]=dp[i-1][j-1]+1
            else:                   # 다를 때
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    
    answer=dp[-1][-1] 
    print(f'#{t} {answer}')

# def solution(a, b): # 최장 공통 부분 수열 알고리즘
#     a = ' ' + a
#     b = ' ' + b
#     an = len(a)
#     bn = len(b)

#     dp = [[0]*an for _ in range(bn)]
#     for i in range(1, bn):
#         for j in range(1, an):
#             if b[i] == a[j]:
#                 dp[i][j] = dp[i-1][j-1] + 1

#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#     #     for row in dp:
#     #         print(row)
#     #     print()
#     # print(dp[-1][-1])
#     return


# if __name__ == "__main__":
#     a0 = input()
#     b0 = input()
#     solution(a0, b0)