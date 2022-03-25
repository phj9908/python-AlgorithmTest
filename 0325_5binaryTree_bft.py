# 이진트리 넓이 우선 순회 알고리즘(breadth First Traversal)
# 재귀X 큐 이용!
#1. traversal=[],q=Queue()
#2. 빈 트리가 아니면 root node를 q에 추가(enqueue)
#3. q가 비어있지 않은 동안
# 3-1) q에서 원소 추출(dequeue)
# 3-2) 그 원소가 자식 노드가 있으면 자식노드들 q에 추가
#4. q가 빈 큐가 되면 모든 노드 방문 완료

class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal=[]
        q=ArrayQueue()
        if self.root:
            q.enqueue(self.root) # 큐에는 노드 자체를 넣기! (노드 데이터가 아닌)
            
        while not q.isEmpty():
            node=q.dequeue()
            traversal.append(node.data) # .data해줌으로써 Node()객체가 됨
            if node.left:   # 주의!) if node.left.data!=None 하면 에러 발생
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
                
        return traversal


def solution(x):
    return 0