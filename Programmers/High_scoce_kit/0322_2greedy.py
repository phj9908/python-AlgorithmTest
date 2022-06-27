# 섬 연결하기
# 최소비용 구하기
# kruskal알고리즘 이용 https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html (kruskal이란)


def solution(n,costs):
    answer=0
    costs.sort(key=lambda x:x[2]) # 비용기준 정렬
    connection=[]
    connection.append(costs[0][0]) # 가장 작은 비용의 출발섬 먼저 넣기
    while len(connection)<n:
        for idx,cost in enumerate(costs):
            if cost[0] in connection and cost[1] in connection:
                continue
            elif cost[0] in connection or cost[1] in connection:
                answer+=cost[2]
                connection.append(cost[0])
                connection.append(cost[1])
                connection=list(set(connection))
                costs.pop(idx)
                break # for문 빠져나오기# 위에서 오름차순 정렬한 상태의 리스트를 pop했기에 elif조건일 때 계속break해도 자연스럽게 다음 원소로 넘어감
    return answer

