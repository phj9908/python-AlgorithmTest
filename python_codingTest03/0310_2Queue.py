# 큐
MAX_QUEUE_SIZE=5

class Queue:
    def __init__(self):
        self.arr=[None]*MAX_QUEUE_SIZE

        self.head=-1 # 가장 오래된 데이터의 인덱스
        self.tail=-1 # 가장 최근 추가된 데이터의 인덱스

    def is_empty(self):
        if self.head==self.tail: # 둘 다 인덱스가 -1
            return True
        return False
    
    def is_full(self):
        if self.tail >=MAX_QUEUE_SIZE-1:
            return True
        return False

    def enqueue(self,item):
        if self.is_full():
            print('큐에 더 이상 데이터를 넣을 수 없습니다.')
        else:
            self.tail+=1 # 삽입할 땐 꼬리쪽에서 추가되는 거니까
            self.arr[self.tail]=item   # arr[tail]=item
        
    def dequeue(self,item):
        if self.is_empty():
            print('큐가 비어있습니다.')
            return None
        else:
            self.head +=1 # 추출할 땐 머리쪽에서 
            return self.arr[self.head]
queue=Queue()

queue.enqueue(1)
