# 미로탈출

MAX_SIZE_QUEUE=50

class Queue:
    def __init__(self):
        self.arr=[None]*MAX_SIZE_QUEUE
        self.head=0
        self.tail=0

    def is_empty(self):
        if self.head== self.tail:
            return True
        return False
    
    def is_full(self):
        if self.tail>=MAX_SIZE_QUEUE-1:
            return True
        return False
    
    def enqueue(self,item):
        if self.is_full():
            print('큐가 이미 가득 찼습니다.')
            return -1
        self.tail = (self.tail+1)%MAX_SIZE_QUEUE
        self.arr[self.tail]=item

    def dequeue(self):
        if self.is_empty():
            print('큐가 비었습니다.')
            return -1
        self.head = (self.head+1)%MAX_SIZE_QUEUE
        return self.arr[self.head]

class Graph:
    def __init__(self):
        self.node_cnt=7
        self.graph=[
            [1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0]
        ]

col,row=map(int,input().split()) 

# 이동 할 네 가지 방향(상,하,좌,우)
dy = [0,0,-1,1]  # y니까 상,하
dx = [-1,1,0,0]  #       좌,우

def BFS(graph,x,y):
    queue=Queue()
    queue.enqueue((x,y))

    while not queue.is_empty():
        x,y = queue.dequeue()
        for i in range(4): # 현재위치에서 4가지 방향으로의 위치 확인
            nx = x +dx[i]
            ny = y +dy[i]
            if nx< 0 or nx >=col or ny<0 or ny>=row: # 미로공간을 벗어난 경우
                continue
            if graph.graph[nx][ny] ==0: # 벽일 때
                continue
            if graph.graph[nx][ny]==1: # 해당 노드를 처음 방문하는 경우에만 (=가중치가 안 더해진 노드)
                graph.graph[nx][ny] = graph.graph[x][y]+1 # +1 가중치 더함
                queue.enqueue((nx,ny)) 
    return graph.graph[col-2][row-1]  # 도착점까지의 최단거리

graph=Graph()
print(BFS(graph,0,0))





    
