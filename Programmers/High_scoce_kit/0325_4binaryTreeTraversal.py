# inorder,preorder, postorder traversal

class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()  # 왼쪽 노드 리스트들 붙이기
        traversal.append(self.data) # 자기자신
        if self.right:
            traversal += self.right.inorder()  # 오른쪽 노드
        return traversal


    def preorder(self):
        traversal=[]
        traversal.append(self.data)
        if self.left:
            traversal+= self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def postorder(self):
        traversal=[]
        if self.left:
            traversal+=self.left.postorder()
        if self.right:
            traversal+=self.right.postorder()
        traversal.append(self.data)
        return traversal


def solution(x):
    return 0