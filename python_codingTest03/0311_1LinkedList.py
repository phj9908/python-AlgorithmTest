# 링크드 리스트
#그냥 array처럼 일렬로 돼있는 게 아니라 원소들이 중구난방으로 있어서 head(출발점,첫번째 원소)에서 두번째 원소(노드)의 주소를 알아내고 두번째 노드에서 세번째노드로 가는 주소를 알아내고...따라서 마지막 n번째 원소까지 갈려면 arr.pop()처럼 못하고 계속 거쳐 거쳐 가야함 시간 복잡도 O(n)

#배열은 인덱스 조회면에선 빠르지만(O(1)) 추가/삭제 면에선 느림(O(n))
#링크드 리스트는 그 반대 > 데이터의 삽입,삭제가 빈번한 곳에서 자주 사용

#https://opentutorials.org/module/1335/8857 개념 참고
####################################################################

#노드 클래스/ 링크드 리스트 클래스 따로 생성
#생성자로 데이터와 포인터받기


class Node:
    def __init__(self,data,next=None): # data만 입력시 pointer초기값은 None
        self.data=data
        self.next=next

#노드 연결해보기
node1 = Node(1)
node2= Node(2)  

head = node1 # 가장 맨 앞 노드 알기위해 head지정
node1.next = node2 # 노드 연결

print(node2.data) # 2
print(node1.next.data)  # 2

class LinkedList(object): # object는 뭐지
    def __init__(self):
        self.head=Node(None) # data=None : 일단 객체 생성시 데이터가 존재하지 않는 노드 생성
        self.size=0 # 노드 갯수
    
    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size ==0:
            return True
        else:
            return False

    def selectNode(self,idx):
        if idx>= self.size:
            print('Index Err')
            return None
        if idx ==0:
            return self.head
        else:
            target = self.head
            for _ in range(idx): # 특정 idx에 도달하면
                target = target.next # (특정 타겟에 도달하면)
            return target        # 반환

    def appendleft(self,data):
        if self.is_empty():
            self.head=Node(data)
        else:
            self.head = Node(data,self.head) # 기존의 head를 두번째로 미루고 그자리에 새로운 data 추가(=맨 앞자리에 추가)
        self.size+=1

    def append(self,data):
        if self.is_empty():
            self.head = Node(data) # 바로 head에 데이터 저장
            self.size +=1
        else:
            target = self.head 
            while target.next: # 마지막node에 도달할 때까지
                target = target.next
            
            target.next=Node(data) # 마지막 node에 다음 노드로 추가
            self.size +=1

    def insert(self,value,idx):
        if self.is_empty():
            self.head=Node(value)
            self.size+=1
        elif idx==0:
            self.head=Node(value,self.head)
            self.size+=1
        else:
            target = self.selectNode(idx-1) # 인덱스3에 삽입하려한다면 인덱스2의 노드 반환
            if target==None:
                return
            new_node = Node(value)

            tmp=target.next
            target.next=new_node
            new_node.next=tmp

            self.size +=1

    def delete(self,idx):
        if self.is_empty():
            print('Empty Linked list')
            return
        elif idx>=self.size:
            print('Index err')
            return
        elif idx==0:
            target = self.head
            self.head = target.next
            del(target)
            self.size -=1
        else:
            target = self.selectNode(idx-1) # 삭제하려는 인덱스의 이전인덱스의 데이터
            deltarget = target.next
            target.next = target.next.next # 삭제 인덱스 이전 데이터의 다음에 삭제인덱스의 다음인덱스를 바로 저장
            del(deltarget)
            self.size -=1
        
    def printlist(self):
        target = self.head
        while target:
            if target.next:
                print(target.data,'->',end='')
                target=target.next
            else:
                print(target.data)
                target=target.next

LL=LinkedList()
LL.append(3)
# print(LL.head) # : <__main__.Node object at 0x0000018BD92A55D0>
node=LL.head
print(node.data) #3