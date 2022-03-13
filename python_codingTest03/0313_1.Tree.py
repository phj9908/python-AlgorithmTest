# 이진트리 
# 계층구조 표현.비선형

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(1)
node_2=Node(2)
node_3=Node(3)
root.left=node_2
root.right=node_3

print(f'루트노드 {root.data}의 자식: {root.left.data}, {root.right.data}')

node_4=Node(4)
node_5=Node(5)
node_2.left=node_4
node_2.right=node_5
print(f'루트노드 왼쪽자식 {root.left.data}의 자식들: {root.left.left.data}, {root.left.right.data}')
