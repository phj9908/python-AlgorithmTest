#이중 링크드 리스트 : 기존 링크드 리스트에서 이전 노드에 접근가능한 버전
# https://opentutorials.org/module/1335/8941 개념 참고


class Node(object):
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Double_LL(object):
    def __init__(self):
        self.head=Node(None)      
        self.tail=self.head # 양쪽 모두 head로 초기화
        self.size = 0
        
    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

    def get(self,idx): # idx위치의 노드 가져오기
        if idx>self.size:
            print('Overflow: Index Err')
            return None
        if idx==self.size:
            return self.tail
        if idx==0:
            return self.head
        if idx <self.size//2:
            target = self.head
            for _ in range(idx):
                target = target.next
                return target
        else: # idx가 리스트 크기 반 이상일 때            
            target = self.tail
            for _ in range(self.size-1,idx,-1): # 역주행
                target = target.prev
            return target

    def append(self,data): # 맨 뒤에 추가
        if self.is_empty():
            self.head=Node(data)
            self.tail=self.head
        else:
            tmp=self.tail # 마지막 원소
            new_node=Node(data,prev=tmp) # 기존 리스트의 마지막값이 새로운 노드를 가리키도록
            tmp.next = new_node
            self.tail=new_node
        self.size +=1
    
    def appendleft(self,data): # 맨 앞에 추가
        if self.is_empty(): 
            self.head = Node(data)
            self.tail=self.head
        else:
            tmp = self.head
            new_node=Node(data,next=tmp) # 새로운노드가 기존의 노드를 가리키도록
            tmp.prev = new_node
            self.head=new_node
        self.size+=1

    def insert(self,data,idx): # idx인덱스에 data추가하기
        if self.is_empty():  
            self.head = Node(data)
            self.tail=self.head
        else:
            tmp = self.get(idx) 
            if tmp==None:
                return
            if tmp==self.head:
                self.appendleft(data)
            elif tmp==self.tail:
                self.append(data)
            else:
                tmp_prev=tmp.prev # idx-1
                new_node=Node(data,tmp_prev,tmp) 
                tmp_prev.next=new_node # (idx-1의 next)= idx 에 new_node 추가
                tmp.prev=new_node # idx
        self.size+=1

    def delete(self,idx): 
        if self.is_empty():
            print('Underflow Err')
            return
        else:
            tmp=self.get(idx)
            if tmp==None:
                return
            elif tmp == self.head:
                tmp= self.head
                self.head=self.head.next
            elif tmp == self.tail:
                tmp=self.tail
                self.tail=self.tail.prev
            else:   # 예: a b c 중 b를 없앤다면
                tmp.prev.next = tmp.next   # a의 next로 c 지정
                tmp.next.prev = tmp.prev   # c의 prev로 a를 지정
            del(tmp)
            self.size -=1
         

    def printlist(self): # 출력 함수
        target = self.head
        while target != self.tail:
            print(target.data,'<->',end=' ') # A <-> B <-> C ...
            target=target.next
        print(target.data) # 마지막 노드
