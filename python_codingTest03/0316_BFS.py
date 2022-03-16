# BFS : 너비 우선 탐색, 두 노드 사이의 최단 경로 탐색시 사용
# 예시)
# 루트 노드 0 을 큐에 넣기
# 0을 빼고 0과 연결된 노드 1,3을 큐에 넣기
# 1을 빼고 1과연결된 노드 2를 넣기
# 2를 빼고 2와 연결된 노드가 없기에 3으로 돌아가
# 3을 빼고 3과 연결된 노드 4,6 넣기
# 4를 빼고 4와 연결된 노드 5넣기
# 5를 빼고 5와 연결된 노드가 없으니 6으로 돌아가
# 6을 빼고 6과 연결된 노드가 없으니 끝

# 원형 큐 이용

MAX_QUEUE_SIZE=10

class Queue:
    def __init__(self):
        self.arr=[None]*MAX_QUEUE_SIZE
        self.head=0 # 가장 오래된 데이터 위치
        self.tail=0 # 가장 최근 추가된 데이터 위치

    def is_empty(self):
        if self.head==self.tail:
            return True
        return False

    def is_full(self):
        if self.tail>=MAX_QUEUE_SIZE-1:
            return True
        return False

    def enqueue(self,item):
        if self.is_full():
            print('큐에 더이상 데이터를 넣을 수 없습니다.')
            return -1

        self.tail = (self.tail+1)%MAX_QUEUE_SIZE # 추가될 원소의 자리(self.tail) 지정
        self.arr[self.tail]=item

    def dequeue(self):
        if self.is_empty():
            print('큐가 비어있습니다.')
            return -1
        self.head=(self.head+1)%MAX_QUEUE_SIZE
        return self.arr[self.head] # 가장 오래된 원소 반환

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
            [0,0,0,1,0,0,0]
        ]
        self.visited_arr=[0]*self.node_cnt

def BFS(graph,node):
    print(node, end=" ")
    graph.visited_arr[node] = 1
    
    queue = Queue()
    queue.enqueue(node)
    while not queue.is_empty():
        delete_node = queue.dequeue()
        for node in range(graph.node_cnt):
            if graph.graph[delete_node][node]==1 and graph.visited_arr[node]==0:
                graph.visited_arr[node]=1 # True
                print(node,end=' ')
                queue.enqueue(node)

graph=Graph()
BFS(graph,0)