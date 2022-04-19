# 볼링공 고르기

# 답안( 책 풀이 참고 )
n,m=map(int,input().split())
arr=list(map(int,input().split()))

weight=[0]*11 # 0부터 11까지 무게별 갯수 저장
for i in arr: 
    weight[i]+=1

answer=0
for i in range(1,len(weight)):
    n-=weight[i] 
    answer+= weight[i]*n # a가 선택한 볼링공 선택 경우의 수 * b가 선택한 ..
print(answer)




# # 내 풀이 (그리디하게 풀진 않음)
# n,m=map(int,input().split())
# arr=list(map(int,input().split()))
# answer=[]

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i]!=arr[j]:
#             answer.append((i,j))
# print(len(answer))