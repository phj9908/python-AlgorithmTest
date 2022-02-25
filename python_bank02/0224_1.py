# 파스칼의 삼각형
# 이중 for문 외에도 11의 거듭제곱을 이용한 풀이도 가능.

n = int(input())
arr =[]

for i in range(n):
    arr.append([]) # 2차원 배열
    arr[i].append(1)  # 시작은 1
    for j in range(1,i):
        arr[i].append(arr[i-1][j]+arr[i-1][j-1])
    if i !=0:
        arr[i].append(1)     # 마지막도 1
for i in range(n):
    print(*arr[i])