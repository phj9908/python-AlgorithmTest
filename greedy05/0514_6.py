# 1931 회의실배정(다시풀기)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
arr=sorted(arr,key=lambda x:(x[1],x[0])) # x[1]가 같으면 x[0]를 기준으로 정렬=> 빨리 끝나는 순으로 정렬

answer = []
answer.append(arr[0][1])
for i in range(1,len(arr)):
    if answer[-1]<=arr[i][0]:
        answer.append(arr[i][1])
print(len(answer))

