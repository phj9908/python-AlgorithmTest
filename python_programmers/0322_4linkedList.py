# 링크드 리스트 순회 구현하기+head부분에 텅 빈 dummy head를 둬서 실제 데이터는 인덱스 1부터 존재하도록 함
# self.data는 append,삭제할 때만 .탐색은 node까지만.(node.next,self.tail,self.head...)

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None) # 원래는 self.head=None 인데 더미헤드 추가로 수정
        self.tail = None
        self.head.next=self.tail    # 더미헤드 추가로 추가된 코드

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        curr_list=[]
        curr=self.head
        #curr_list.append(cuur.data) # 이거때문에 시간초과남. curr=self.head로 head만 잡아주고 넣는건 while에서 다 하기!!!

        while curr.next:
            curr=curr.next  # head는 빈 노드이기에 한번더 next
            curr_list.append(curr.data)
        return curr_list

    def insertAfter(self,prev,newNode): # prev의 next에 newNode 삽입
        newNode.next=prev.next
        if prev.next is None:
            self.tail=newNode
        prev.next=newNode
        self.nodeCount +=1
        return True
        
    def insertAt(self,pos,newNode):
        if pos <1 or pos>self.nodeCount+1: 
            return False
        if pos!=1 and pos==self.nodeCount+1: # tail 뒤에 삽입하려는 경우,pos=1이면서 pos=self.nodeCount+1일땐  빈 노드에 추가하는것이라서 안됨
            prev=self.tail
        else:
            prev=self.getAt(pos-1)
        return self.insertAfter(prev,newNode)

        # prev가 마지막 노드일 때 prev.next==None
        #  삭제할 노드 없음
        #  return None
        #  리스트 맨 끝의 node를 삭제 할때 curr.next=None
        #  tail조정 필요
    def popAfter(self,prev):
        curr=prev.next
        if prev.next==self.tail: # tail을 없애는 경우
            prev.next=None
            self.tail=prev
        else:
            prev.next=curr.next
        self.nodeCount-=1
        return curr.data

    def popAt(self, pos):
        if pos <1 or pos > self.nodeCount:
            raise IndexError
        prev=self.getAt(pos-1)
        return self.popAfter(prev)


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0