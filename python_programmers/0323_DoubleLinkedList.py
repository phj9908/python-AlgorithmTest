# head뿐만 아니라 tail도 dummy로 만들기(빈노드로 만들기)


class Node:
    def __init__(self,item):
        self.data=item
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.tail.next=None

    def reverse(self):  
        curr_list=[]
        curr=self.tail
        while curr.prev:
            curr=curr.prev # tail이 빈 노드이기에 prev한 칸 더
            curr_list.append(curr.data)
        return curr_list

    def concat(self,L):     # 두 개의 LL병합 : self.head<-...->L.tail /self.tail과 L.head는 생략
        self.tail.prev.next=L.head.next
        L.head.next.prev=self.tail.prev

        self.tail=L.tail
        self.nodeCount+=L.nodeCount

    def getAt(self,pos):
        if pos<0 or pos>self.nodeCount:
            return None
        if pos>self.nodeCount//2:
            i=0
            curr=self.tail
            while i<(self.nodeCount -pos )+1: # 반복문에서 prev로 접근할거라서 pos+1인덱스까지
                curr=curr.prev
                i+=1
        else:
            i=0
            curr=self.head
            while i<pos:
                curr=curr.next
                i+=1
        return curr
    
    def insertBefore(self,next,newNode):
        prev=next.prev
        newNode.next=next
        newNode.prev=prev
        next.prev=newNode
        prev.next=newNode
        self.nodeCount+=1
        return True

    def insertAfter(self,prev,newNode):
        next=prev.next
        newNode.prev = prev
        newNode.next=next
        prev.next=newNode
        next.prev=newNode
        self.nodeCount+=1
        return True

    def insertAt(self,pos,newNode):
        if pos<1 or pos>self.nodeCount+1:
            return False
        prev=self.getAt(pos-1)
        return self.insertAfter(prev,newNode)

    def popAfter(self, prev):
            curr=prev.next
            next=curr.next
            # if prev.next==self.tail:
            #     return None # tail은 이미 빈노드니까 
            
            prev.next=next # next로 가는 node개선
            next.prev=prev # prev로 가는 node개선
            
            self.nodeCount-=1
            return curr.data

    def popBefore(self, next):
        curr=next.prev
        prev=curr.prev
        # if next.prev==self.head:
        #     return None # head는 이미 빈 노드

        prev.next=next # next로 가는 node 개선
        next.prev=prev # prev로 가는 node 개선
        
        self.nodeCount-=1
        return curr.data

    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError
        # if pos ==1:
        #     return self.popAfter(self.head)
        else:
            prev=self.getAt(pos-1)
            #next_node=self.getAt(pos+1)

        return self.popAfter(prev) # popBefore로 하면 통과안되는 게 있다.
