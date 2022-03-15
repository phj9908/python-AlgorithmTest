# 순회 결과로 트리 재구성 
# 전위,중위 순회 결과로 후위순회 결과 출력
# https://ihp001.tistory.com/106

from typing import List

class Node():
    def __init__(self,data=0):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def buildTree(self,preorder:List,inorder:List):
        if inorder:
            index = inorder.index(preorder.pop(0)) # 전위순회 결과 맨앞 원소는 최상단원소

            # 최상단 원소를 기준으로 중위순회 결과값을 최상단 원소의 left,right로 분할
            node = Node(inorder[index])
            node.left= self.buildTree(preorder,inorder[0:index]) 
            node.right = self.buildTree(preorder,inorder[index+1:])

            return node

def post_order(node):
    if node==None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f'{node.data}',end=' ')

preorder_arr=list(map(int,input('전위 순회 결과: ').split()))
inorder_arr=list(map(int,input('중위 순회 결과: ').split()))

tree=Solution()
post_order(tree.buildTree(preorder_arr,inorder_arr))