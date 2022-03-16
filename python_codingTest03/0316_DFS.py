# 그래프 탐색 ( dfs/bfs )
# dfs: 깊이 우선 탐색, 모든 노드를 탐색하는 경우 사용
# 재귀 이용

class Graph:
    def __init__(self):
        self.node_cnt=7
        self.graph=[
            [0,1,0,1,0,0,0], 
            [1,0,1,0,0,0,0],
            [0,1,0,0,0,0,0],
            [1,0,0,0,1,0,1],
            [0,0,0,1,0,1,0],
            [0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0],
        ]
        self.visited_arr=[0]*self.node_cnt

def DFS(graph,node):
    print(node,end='')
    graph.visited[node]=1

    for i in range(graph.node_cnt):
        if graph.graph[node][i] ==1 and graph.visited_arr[i]==0:
            DFS(graph,i)

graph=Graph()
graph.visited_arr[0]=1
DFS(graph,0)

# class Graph:
#     def __init__(self):
#         self.node_count = 7 
#         self.graph = [
#             [0, 1, 0, 1, 0, 0, 0], # 0은 1과 3이랑 연결 ...
#             [1, 0, 1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 1, 0, 1],
#             [0, 0, 0, 1, 0, 1, 0],
#             [0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#         ]
#         self.visited_arr = [0] * self.node_count # 열 별로 방문 여부를 배열에 저장

# def DFS(graph, node):
#     print(node, end=" ")
#     graph.visited_arr[node] = 1

#     for i in range(0, graph.node_count):
#         if graph.graph[node][i] == 1 and graph.visited_arr[i] == 0: # 연결된 노드가 있고 그 노드는 방문 안했다면
#         # (ex) node=4이고 i=3일 때, graph.graph[node][i]==1, graph.visited_arr[i]==1 이기에 빠져나옴 
#         # 근데 node =4이고 i=5일 때 graph[node][i]==1, graph.visited_arr[i]==0 이기에 재귀 실행
#             DFS(graph, i)

# graph = Graph()
# graph.visited_arr[0] = 1 
# DFS(graph, 0)
