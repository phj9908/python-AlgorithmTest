# 숫자 카드 게임
n,m=map(int,input().split())
arr=[ list(map(int,input().split())) for i in range(n)]
answer=min(arr[0])
for i in range(1,n):
    if answer<min(arr[i]):
        answer=min(arr[i])
print(answer)
