# 10971 외판원 순회2 : 여러 도시중에서 한 도시 중에 다른도시로 이동하는 최소비용의 이동순서 도출, 각 도시는 한번만 방문+ 원래 시작점에 돌아오기
# 나중에 책 한번 보기

import sys

n = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(n)]
min_value = sys.maxsize 

def dfs_backtracking(start, curr, value, s): #시작도시,현재도시,비용, 방문한 도시
    global min_value

    if len(s) == n: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[curr][start] != 0: #마지막 도시에서 출발 도시로 갈 수 있다면
            min_value = min(min_value, value + travel_cost[curr][start]) 
        return

    for i in range(n): #도시의 개수 만큼 반복
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[curr][i] != 0 and i not in s and value < min_value:  
            s.append(i) 
            dfs_backtracking(start, i, value + travel_cost[curr][i], s) # i번째 도시 방문
            s.pop() 


#도시마다 출발점을 지정 (i번째 도시의 출발점은 W[i][i]이다,항상 0이다)
for i in range(n):
    dfs_backtracking(i, i, 0, [i])

print(min_value)