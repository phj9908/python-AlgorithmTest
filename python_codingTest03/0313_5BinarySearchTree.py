# 중요!!
# 이진트리의 데이터 탐색과 삽입
#https://codemate.kr/project/%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-Level-1/12-2.-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%90%EC%83%89%EA%B3%BC-%EC%82%BD%EC%9E%85

# 크기 비교는 높이마다 하기에 O(n)이 아닌 O(h) 시간 소요

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree():
    def __init__(self):
        self.root =None

    def set_root(self,data):
        self.root=Node(data) # 맨 처음 노드값

    def find_node_by_data(self,current_node,data): # 목표값과 노드간의 크기 비교
        if current_node==None:
            return False
        if data == current_node.data:
            return current_node
        if data < current_node.data: # 목표값보다 현 노드값이 더 크면
            return self.find_node_by_data(current_node.left,data) # 현 노드의 왼쪽자식노드랑 비교
        if data > current_node.data:
            return self.find_node_by_data(current_node.right,data)
    
    def find(self,data): # 목표값을 가지는 노드가 존재하는지 탐색 결과 반환
        if self.find_node_by_data(self.root,data)==False: 
            return False
        else:
            return True

    def insert_node(self,current_node,data): # 삽입값의 자리를 찾기위해 재귀 탐색
        if data<current_node.data:
            if current_node.left ==None:
                current_node.left=Node(data)
            else:
                self.insert_node(current_node.left,data)
        elif data>current_node.data:
            if current_node.right ==None:
                current_node.right=Node(data)
            else:
                self.insert_node(current_node.right,data)
        else:
            if data == current_node.data:
                print(f'이미 {data}의 값이 존재합니다. 중복된 값은 삽입할 수 없습니다.')
                return

    def insert(self,data):
        if self.root==None:
            self.set_root(data)
        else:
            self.insert_node(self.root,data)

    # def temp_data_insert(root): # 데이터 삽입 임시 함수
    #     node_2=Node(2)
    #     node_3=Node(10)
    #     root.left=node_2
    #     root.right=node_3
    #
    #     return root

    def get_next_node(self,node): # 해당 노드의 왼쪽 노드만 파기 (= 최솟값 도출) 
        while node.left:
            node=node.left
        return node

    def delete_node(self,parent,current_node,data):
        if current_node==None:
            print(f'트리에 {data}가 존재하지 않습니다.')
            return
        if data<current_node.data:
            self.delete_node(current_node,current_node.left,data)
        elif data>current_node.data:
            self.delete_node(current_node,current_node.right,data)
        else: # 삭제 대상 노드에 도달했다면
            if current_node.left==None and current_node.right ==None: # 대상 노드에 자식노드가 없다면
                if data< parent.data: # 대상노드가 왼쪽노드일 때
                    parent.left=None
                else:
                    parent.right=None
            elif current_node.left!=None and current_node.right==None: # 대상노드에 왼쪽 자식노드가 있다면
                if data<parent.data:
                    parent.left=current_node.left
                else:
                    parent.right=current_node.left # 이거 그려보면 이해감
            elif current_node.left ==None and current_node.right!=None:
                if data< parent.data:
                    parent.left=current_node.right
                else:
                    parent.right=current_node.right
            elif current_node.left!=None and current_node.right!=None:
                
                next_node=self.get_next_node(current_node.right) # 대상노드의 오른쪽 자식노드중 최솟값 갖는 노드 도출
                current_node.data=next_node.data # 대상노드와 대상노드의 오른쪽 자식노드 중 최솟값 노드 스왑
                self.delete_node(current_node,current_node.right,next_node.data)
                # 원래 최솟값 노드 자리 없애기

    def delete(self,data):
        if self.root==None:
            print('트리에 노드가 존재하지 않습니다.')
        else:
            self.delete_node(None,self.root,data)


def in_order(node):
    if node==None:
        return
    in_order(node.left)
    print(f'{node.data}',end=' ')
    in_order(node.right)

BST=BinarySearchTree()
BST.set_root(7) 
#BST.root=temp_data_insert(BST.root)
BST.insert(3)
BST.insert(1)
BST.insert(5)

print('root -> left -> left:',BST.root.left.left.data)
print('root -> left-> right:', BST.root.left.right.data)

BST.delete(1)
in_order(BST.root)
    