# 트리 탐색 : 전위 순회/ 중위 순회/ 후위 순회
# https://codemate.kr/project/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-Level-1/11-2.-%ED%8A%B8%EB%A6%AC%EC%9D%98-%ED%83%90%EC%83%89

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def get_sample():
    root=Node(1)
    node_2=Node(2)
    node_3=Node(3)
    root.left=node_2
    root.right=node_3

    node_4=Node(4)
    node_5=Node(5)
    node_2.left=node_4
    node_2.right=node_5

    return root

def pre_order(node): # 부모노드 부터(최상단 부터)
    if node==None:
        return
        
    print(f'{node.data}',end=' ')
    pre_order(node.left)
    pre_order(node.right)

root=get_sample()
pre_order(root)

def in_order(node): # 왼쪽 자식노드 부터(최하단 좌측부터)
    if node==None:
        return
    
    in_order(node.left) # 최하단까지 도달
    print(f'{node.data}',end=' ')
    in_order(node.right)

in_order(root)

def post_order(node): # 왼쪽 자식노드 부터(최하단 좌측부터)
    if node==None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f'{node.data}',end=' ')

post_order(root)