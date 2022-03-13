# 이진탐색의 장점 + 링크드리스트의 장점>>이진트리
# 탐색 O(log n) + 자료 입력,삭제 O(1)의 시간복잡도 소요

# 왼쪽 자식만 타고내려가다보면 최소값 발견
# 오르쪽 자신만                최대값

# 가장 왼쪽 노드에서 출발해서 가장 오른쪽 노드에서 탐색을 종료하는 중위순회시 오름차순으로 데이터 방문하는것!

### Node는 self.data=data이지만 BST에선 self.root.data=data 해줘야 함 이때 root는 최상단 노드

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None  

    def set_root(self,data):
        self.root=Node(data)

BST=BinarySearchTree()
BST.set_root(1)
print(BST.root.data)
        
        
