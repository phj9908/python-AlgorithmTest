# 2304 창고다각형(while 문썼더니 입력답안은 맞지만 결과적으론 틀림.
# for문 으로 다시풀기)

n = int(input())
arr = []
endX, maxY, maxX = 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))
    endX=max(endX,x) # 필요한 arr길이
    if maxY < y:
        maxY = y  # 가장 높은 기둥 길이
        maxX = x  #             의 인덱스

sum = 0
temp = 0
for i in range(maxX + 1):  # 가장높은 기둥까지 포함해서 다각형 면적 구하기
    if arr[i] > temp:
        temp = arr[i]
    sum += temp

temp = 0
for i in range(endX, maxX, -1):  # 가장 높은 기둥까지 역방향으로 면적구하기
    if arr[i] > temp:
        temp = arr[i]
    sum += temp

print(sum)

# # 15l~26l까지 풀이와 다른 풀이>> 스택
# stack=[]
# for i in range(maxX+1):
#     if not stack:
#         stack.append(arr[i])
#     else:
#         if stack[-1]<arr[i]:
#             stack.pop()
#             stack.append(arr[i])
#     sum+=stack[-1]
#
# stack=[]
# for i in range(endX,maxX,-1):
#     if not stack:
#         stack.append(arr[i])
#     else:
#         if stack[-1] < arr[i]:
#             stack.pop()
#             stack.append(arr[i])
#     sum+=stack[-1]