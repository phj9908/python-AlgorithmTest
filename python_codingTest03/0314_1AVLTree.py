# AVL 트리: 트리의 균형을 맞춰줌, 한쪽으로 편향된 이진트리가 되면 노드수와 트리의 높이가 비례하게 증가하기에 이를 방지
#회전 연산 코드 및 그림 :https://blog.naver.com/beaqon/221298022121
# 코드 참고 :https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=beaqon&logNo=221298914412 여기서 key는 data역할이고 value는 뭐지 key만 있는 버전으로 수정하던가
# 그냥 이진트리와 달리 AVL은 데이터 넣으면서 균형을 맞추니까 set_root()가 의미없음

class Node():
    def __init__(self,data,height):
        self.data=data
        self.left=None
        self.right=None
        self.height=height
    
class AVL():
    def __init__(self):
        self.root=None

    def height(self,node):
        if node==None:
            return 0
        return node.height

    def height_dif(self,node):
        return self.height(node.left)-self.height(node.right)
    
    def rotate_right(self,current_node):
        x_node= current_node.left 
        current_node.left = x_node.right # x에 오른쪽 자식노드를 현재노드의 왼쪽자식으로 둠
        x_node.right = current_node # current_node가 x_node 서브트리로 내려감 (그림 참고!)
        
        current_node.height = max(self.height(current_node.left),self.height(current_node.right))+1 # 높이 갱신
        x_node.height = max(self.height(x_node.left),self.height(x_node.right))+1
        
        return x_node # 회전 후 x_node가 current_node의 이전자리로 이동되었으므로

    def rotate_left(self,current_node): 
        x_node= current_node.right
        current_node.right = x_node.left
        x_node.left = current_node
        
        current_node.height = max(self.height(current_node.left),self.height(current_node.right))+1
        x_node.height=max(self.height(x_node.left),self.height(x_node.right))+1

        return x_node
    
    def balance(self,current_node):

        if self.height_dif(current_node) > 1: # 왼쪽 서브트리 불균형(현 노드의 불균형 판단은 절댓값 2이상이면 불균형, 1보다 크면 왼쪽 불균형, -1보다 작으면 오른쪽 불균형)
            if self.height_dif(current_node.left) < 0 : # 왼쪽 서브트리의 오른쪽 서브트리가 불균형일 때,(자식노드의 불균형 판단은 음수양수 여부로)
                current_node.left = self.rotate_left(current_node.left)
            current_node = self.rotate_right(current_node)
        
        elif self.height_dif(current_node) < -1:
            if self.height_dif(current_node.right) > 0 : # 오른쪽 서브트리의 왼쪽서브트리가 불균형일 때
                current_node.right=self.rotate_right(current_node.right)
            current_node = self.rotate_left(current_node)
        
        return current_node

    def insert_node(self,current_node,data):
        if current_node == None:
            return Node(data,1) # data값을 가진 높이 1의 Node
        if current_node.data > data:
            current_node.left=self.insert_node(current_node.left,data)
        elif current_node.data< data:
            current_node.right= self.insert_node(current_node.right,data)
        elif data == current_node.data:
            print(f'이미 {data}의 값이 존재합니다. 중복된 값은 삽입할 수 없습니다.')
            return
        current_node.height = max(self.height(current_node.left),self.height(current_node.right))+1
        
        return self.balance(current_node)

    def insert(self,data):
        self.root=self.insert_node(self.root,data)

def in_order(node):
    if node==None:
        return
    in_order(node.left)
    print(f'{node.data}',end=' ')
    in_order(node.right)

AVL_tree=AVL()   
AVL_tree.insert(10)
AVL_tree.insert(20)
AVL_tree.insert(30)
AVL_tree.insert(40)
AVL_tree.insert(50)
AVL_tree.insert(29)
in_order(AVL_tree.root)

