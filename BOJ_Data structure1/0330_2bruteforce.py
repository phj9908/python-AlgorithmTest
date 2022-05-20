# 사탕게임
# 자리바꾸고 / 탐색해서 최댓값 갱신 / 자리 원위치 과정 반복
# arr[y][x]

n= int(input())
arr=[ list(input()) for i in range(n)]
answer=0

def check(arr):
    temp=1
    for i in range(n):
        cnt=1
        for j in range(n):
            if j-1 >=0:
                if arr[i][j-1]==arr[i][j]:# 이전 것과 같다면 
                    cnt+=1
                else:
                    cnt=1 # 이전과 다르다면 다시 1로 초기화
                temp=max(temp,cnt) # 현재 cnt가 더 크면 answer갱신
        cnt=1
        for j in range(n):
            if j-1 >=0:
                if arr[j-1][i]==arr[j][i]:
                    cnt+=1
                else:
                    cnt=1
                temp=max(temp,cnt)
    return temp

for i in range(n):
    for j in range(n):
        if j+1 <n:
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j] # 인접한 자리끼리 바꾸기
            temp=check(arr)# 탐색해서 최댓값 확인
            answer=max(answer,temp)
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j] # 자리 원위치

            arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
            temp=check(arr)
            answer=max(answer,temp)
            arr[j][i],arr[j+1][i]=arr[j+1][i],arr[j][i]
print(answer)