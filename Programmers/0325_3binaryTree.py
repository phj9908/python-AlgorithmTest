# Node클래스로 이진트리 클래스 구현

class Node:
    def __init__(self,item):
        self.data=item
        self.left=None
        self.right=None

    def size(self): # 재귀적으로 호출
        l= self.left.size() if self.left else 0
        r= self.right.size() if self.right else 0
        return l+r+1

    def depth(self): # 재귀
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l,r)+1 # right,left 둘중 더 깊은레벨 + 자기자신

class BinaryTree:

    def __init__(self, r:Node):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size() # 이때 size()는 class Node의 메서드임!
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()  # 이때 depth()는 class Node의 메서드임
        else:
            return 0


def solution(x):
    return 0
        