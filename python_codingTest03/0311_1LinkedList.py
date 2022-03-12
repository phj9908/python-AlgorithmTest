# 링크드 리스트
#그냥 array처럼 일렬로 돼있는 게 아니라 원소들이 중구난방으로 있어서 head(출발점,첫번째 원소)에서 두번째 원소(노드)의 주소를 알아내고 두번째 노드에서 세번째노드로 가는 주소를 알아내고...따라서 마지막 n번째 원소까지 갈려면 arr.pop()처럼 못하고 계속 거쳐 거쳐 가야함 시간 복잡도 O(n)

#http://visualgo.net 링크드 리스트 시각화해서 볼 수 있음

#배열은 인덱스 조회면에선 빠르지만(O(1)) 추가/삭제 면에선 느림(O(n))
#링크드 리스트는 그 반대 > 데이터의 삽입,삭제가 빈번한 곳에서 자주 사용

####################################################################

#노드 클래스/ 링크드 리스트 클래스 따로 생성
#생성자로 데이터와 포인터받기

class Node:
    def __init__(self,data,pointer=None): # data만 입력시 pointer초기값은 None
        self.data=data
        self.pointer=pointer # or next

#노드 연결해보기
node1 = Node(1)
node2= Node(2)  

head = node1 # 가장 맨 앞 노드 알기위해 head지정
node1.pointer = node2 # 노드 연결

print(node2.data) # 2
print(node1.pointer.data)  # 2

class LinkedList(object): # object는 뭐지
    def __init__(self):
        self.head=Node(None) # data=None : 일단 객체 생성시 데이터가 존재하지 않는 노드 생성
        self.size=0 # 노드 갯수
    
    def append(self,data):
        if self.size==0: # 아무 노드가 없으면
            self.head = Node(data) # 바로 head에 데이터 저장
            self.size +=1
        else:
            node = self.head 
            while node.pointer: # 마지막node에 도달할 때까지
                node = node.pointer
            
            node.pointer=Node(data) # 마지막 node에 다음 노드로 추가
            self.size +=1

LL=LinkedList()
LL.append(3)
# print(LL.head) # : <__main__.Node object at 0x0000018BD92A55D0>
node=LL.head
print(node.data) #3
LL.append(4)
print(node.pointer)








