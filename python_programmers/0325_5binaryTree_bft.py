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

# 위 반복문 안에서 if문을 쓸 때 'if node.left:'를 쓰면 통과가 되고 'if node.left.data!=None' 을 쓰면 에러가 나는 이유
# 어떤 노드 (node) 의 "왼쪽 자식이 존재하는가" 의 조건을 검사하는 표현식으로서 node.left 를 적용했습니다. 만약 이 노드의 왼쪽 자식이 존재한다면 node.left 에 담긴 객체는 class Node 의 객체 인스턴스로서 왼쪽 자식 노드에 해당할 것입니다. 그렇지 않다면, 즉 왼쪽 자식이 존재하지 않는 경우라면, 여기에는 None 이 담겨 있게 됩니다. 그 이유는, Node.__init__(), 즉 class Node 의 생성자 (constructor) 에서 self.left = None (L26) 으로 했으므로 node 가 생성될 때 node.left = None 이 되었으며 그 이후에 여기에 다른 것을 대입한 적이 없기 때문입니다.

# 따라서, L45 의 조건문에서 node.left 라고 한 것을 node.left == None 이라고 바꾸어 쓸 수도 있습니다. Python 에서는 조건식의 값이 None 이면 이것은 거짓 (False) 으로 간주됨을 이용한 것으로서, 전자의 표현이 후자의 표현보다 "왼쪽 자식이 있는가" 를 보다 직관적으로 나타내기 때문에 이와 같이 표현한 것입니다.

# ***한편, node.left.data != None 은 런타임 에러의 가능성이 있습니다. 위에 언급한 것처럼, node 가 왼쪽 자식을 가지지 않는 경우에는 node.left == None 이고, 그렇다면 node.left.data 는 "None 객체의 left 라는 속성" 을 가리키게 되는데, None 객체에는 left 라는 속성이 없으므로 AttributeError 의 예외가 발생하게 됩니다.*** 

# 또 하나의 사족을 붙인다면, node 의 왼쪽 자식이 있는 경우에는 node.left.data != None 은 이것을 올바르게 판단할 것입니다. 왜냐면 우리가 이 예에서는 각 노드의 데이터 원소에 None 을 넣지 않기 때문입니다. 하지만, 데이터 원소가 None 인 응용을 완전히 배제할 수는 없다는 이유로도 이 표현은 좋다고 할 수는 없겠습니다.

