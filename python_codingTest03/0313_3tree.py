# 트리의 최하단 노드 값 출력 & 레벨 출력
# 수정해야함.하다말음

import collections


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.depth=0

    def get_size(self): # 재귀 이용, 노드갯수 
        l_size=self.left.size() if self.left else 0
        r_size=self.right.size() if self.right else 0

        return l_size+r_size+1 # 1은 자기 자신

    def get_height(self):
        l_height=self.left.get_height() if self.left else 0
        r_height=self.right.get_height()  if self.right else 0

        return max(l_height,r_height)+1


def get_sample():
    root=Node(7)
    node_2=Node(3)
    node_3=Node(10)
    root.left=node_2
    root.right=node_3

    node_4=Node(1)
    node_5=Node(5)
    node_2.left=node_4
    node_2.right=node_5

    node_6=Node(8)
    node_3.left=node_6

    node_7=Node(4)
    node_8=Node(12)
    node_5.left=node_7
    node_7.left=node_8

    return root

def pre_order(node): # 부모노드 부터(최상단 부터)
    if node==None:
        return

    if node.get_height()== 1: #??수정하기
        print(f'최하단 노드: {node.data}')
    
    pre_order(node.left)
    pre_order(node.right)

root=get_sample()
pre_order(root)
print(root.get_height())
print(root.get_size())