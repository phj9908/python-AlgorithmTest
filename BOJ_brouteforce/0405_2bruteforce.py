# 10971 외판원 순회2 : 여러 도시중에서 한 도시 중에 다른도시로 이동하는 최소비용의 이동순서 도출, 각 도시는 한번만 방문+ 원래 시작점에 돌아오기
# https://www.youtube.com/watch?v=-zb54MpMgBY 15:26 참고
# n개의 도시 순회 => 0부터 N-1까지의 수열 dfs (s[]에는 0~n-1의 수만 저장됨)
# 주의! 외판원은 모든 입력행렬이 한 스테이지가 아님 한 줄임 입력을 한번에 받아서 2차원 배열로 받는거임

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
s=[]
answer=987654321

def dfs(start,curr,value):
    global answer
    if len(s)==n:
        print(*s) # 디버깅용
        if arr[curr][start]!=0: #마지막 도시에서 출발 도시로 갈 수 있다면
            answer=min(answer,value+arr[curr][start])
        return
    for i in range(n):  #도시의 개수 만큼 반복
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if arr[curr][i]!=0 and i not in s and value<answer:
            s.append(i)
            dfs(start,i,value+arr[curr][i])  # i번째 도시 방문
            s.pop()

#도시마다 출발점을 지정 (i번째 도시의 출발점은 W[i][i]이다,항상 0이다)
for i in range(n):
    s=[i] # 출발점 저장
    print(f'start: ({i},{i})') # 디버깅용
    dfs(i,i,0)
print(answer)