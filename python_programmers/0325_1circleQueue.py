class CircularQueue:
    def __init__(self,n):
        self.maxCount=n
        self.data=[None]*self.maxCount
        self.count=0
        self.front=-1 # dequeue할 때 제거되는 위치(가장 오래된 원소 위치)
        self.rear=-1 # enqueue할 때 삽입되는 위치(가장 최근의원소 위치)

    #front,rear위치 초기화값 -1이어야 하는 이유
    #self.front = (self.front+1)%self.maxCount 
    #self.rear=(self.rear+1)%self.maxCount

    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self,x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear=(self.rear+1)%self.maxCount
        self.data[self.rear]=x
        self.count+=1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue is Empty')
        self.front = (self.front+1)%self.maxCount
        x=self.data[self.front]
        self.count-=1

        return x