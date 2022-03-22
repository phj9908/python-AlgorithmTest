# 링크드 리스트 순회 구현하기
# traverse(),popAt() 구현
# self.data는 append할 때만 . 삭제나 탐색은 node까지만.(node.next,self.tail,self.head...)

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        if self.nodeCount==0:
            return []
        
        curr_list=[]
        curr=self.head
        #curr_list.append(cuur.data) # 이거때문에 시간초과남. curr=self.head로 head만 잡아주고 넣는건 while에서 다 하기!!!

        while curr:
            curr_list.append(curr.data)
            curr=curr.next       
        return curr_list
        
    def popAt(self, pos):
            del_data=0
            if pos<1 or pos>self.nodeCount:
                raise IndexError
                
            if self.nodeCount==1:
                del_data=self.head.data
                self.head=None
                self.tail=None
            
            else:
                if pos==1:
                    del_data=self.head.data
                    self.head=self.head.next
                    #del(del_item)
                
                elif pos==self.nodeCount: # 노드 중간 데이터나 tail에 데이터 꺼내기는 같은 시간 복잡도 O(n)
                    prev=self.getAt(pos-1) 
                    del_data=prev.next.data
                    del(prev.next) # = prev.next=None
                    self.tail=prev
                else:
                    prev=self.getAt(pos-1) 
                    del_data=prev.next.data
                    #del(prev.next) # = prev.next=None
                    prev.next=prev.next.next
            self.nodeCount-=1
            return del_data


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0