# 볼링공 고르기

# 답안( 책 풀이참고 )
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

# # 내풀이 (count()활용)
# arr.sort()
# for i in arr:
#     x=arr.count(i)
#     answer+=n-x
#     arr.popleft()
# print(answer)