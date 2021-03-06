# 이진 탐색 트리: 왼쪽 원소는 부모노드보다 작고, 오른쪽 원소는 부모노드보다 크도록 구성된 이진트리

# key들을 이진트리로 구성(key값 크기 비교하여 이진트리 구성)

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        node=Node(key,data)
        
        if key<self.key:
            if self.left: # 왼쪽 자식노드가 이미 있다면 
                return self.left.insert(key,data)
            else: # 왼쪽 노드가 없다면
                self.left=node # 만들었던 새 노드를 붙이기
                
        elif key>self.key:
            if self.right:
                return self.right.insert(key,data)
            else:
                self.right=node
                
        elif key==self.key: # 중복된 키는 있을 수 없음
            raise KeyError('...')
    
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left == None
                    elif parent.right == node:
                        parent.right == None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    nodeChild = node.left
                else:
                    nodeChild = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left is node:
                        parent.left = nodeChild
                    else:
                        parent.right = nodeChild
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = nodeChild
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right # 해당 node보다 큰 값중에 최솟값 찾기 위함!
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로

                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left: # 해당 노드의 오른쪽 서브트리중 제일 하단의 왼쪽 노드 찾기
                    parent = successor
                    successor = parent.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.(successor를 제거)
                if parent.left == successor:
                    if successor.right: # successor의 오른똑 자식이 있을 때
                        parent.left = successor.right
                    else: # 아예자식이 없을 때
                        parent.left = None
                if parent.right == successor:
                    if successor.right:
                        parent.right = successor.right
                    else:
                        parent.right=None
            return True

        else:
            return False

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

def solution(x):
    return 0