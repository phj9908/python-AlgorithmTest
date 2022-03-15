class Graph:
    def __init__(self):
        self.node_count = 7 
        self.graph = [
            [0, 1, 0, 1, 0, 0, 0], # 0은 1과 3이랑 연결 ...
            [1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ]
        self.visited_arr = [0] * self.node_count # 열 별로 방문 여부를 배열에 저장

def DFS(graph, node):
    print(node, end=" ")
    graph.visited_arr[node] = 1

    for i in range(0, graph.node_count):
        if graph.graph[node][i] == 1 and graph.visited_arr[i] == 0: # 자식노드가 있고 그 열은 방문안했다면
            DFS(graph, i)

graph = Graph()
graph.visited_arr[0] = 1 
DFS(graph, 0)
