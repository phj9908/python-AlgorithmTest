# 사탕게임
# 자리바꾸고 / 탐색해서 최댓값 갱신 / 자리 원위치 과정 반복
# arr[y][x]

def check(arr):
    n=len(arr)
    answer=1

    for i in range(n):
        cnt=1    
        for j in range(1,n):
            if arr[i][j] ==arr[i][j-1]: # 이전 것과 같다면 
                cnt+=1
            else:
                cnt=1 # 이전과 다르다면 다시 1로 초기화
            if cnt>answer: 
                answer=cnt  # 현재 cnt가 더 크면 answer갱신
        
        cnt=1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt+1
            else:
                cnt=1
            if cnt> answer:
                answer=cnt
    return answer

n = int(input())
arr=[]
for _ in range(n):
    arr.append(list(input()))
answer=0
for i in range(n):
    for j in range(n):
        if j+1<n:
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j] # 인접한 자리끼리 바꾸기
        
            temp=check(arr) # 탐색해서 최댓값 확인
            if temp>answer:
                answer=temp
        
            arr[i][j],arr[i][j+1]=arr[i][j+1],arr[i][j] # 자리 원위치

        if i+1<n:
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]
        
            temp=check(arr)
            if temp>answer:
                answer=temp
        
            arr[i][j],arr[i+1][j]=arr[i+1][j],arr[i][j]

print(answer)

 