# 원형 큐 (그림 참고 https://blog.naver.com/sooftware/221512458414)
# 큐의 크기가 5일 때, 인덱스가 4를 넘어가면 선형 큐에서는 오류가 발생(실제론 0부터 4까지의 인덱스만 존재하기에)
# 선형 큐와 달리 head, tail이 배열의 마지막 인덱스에 도착하면 다시배열의 첫 부분으로 돌려줌(크기가 5일 때 인덱스 4를 넘어가면 (4+1)%5=0 으로 인덱스 0에 데이터 할당 )

# 우선 순위가 필요한 인쇄 대기열이나 bfs,dfs에서 처리할 노드 리스트 저장용도로 잘 쓰인다. 단독으로 큐 문제는 잘 안나옴


MAX_QUEUE_SIZE=5

class Queue:
    def __init__(self):
        self.arr=[None]*MAX_QUEUE_SIZE

        self.head=0 # 가장 오래된 데이터의 인덱스
        self.tail=0 # 가장 최근 추가된 데이터 인덱스

    def is_empty(self):
        if self.head==self.head:
            return True
        return False
    
    def is_full(self):
        if self.tail>=MAX_QUEUE_SIZE-1:
            return True
        return False

    def enqueue(self,item):
        if self.is_full():
            print('큐에 더 이상 데이터를 넣을 수 없습니다.')
        else:
            self.tail=(self.tail+1)%MAX_QUEUE_SIZE
            self.arr[self.tail]=item # arr[tail]=item

    def dequeue(self,item):
        if self.is_empty():
            print('큐가 비어있습니다.')
        else:
            self.head= (self.head+1)%MAX_QUEUE_SIZE
            return self.arr[self.head]

queue=Queue()

queue.enqueue(1)
queue.enqueue(2)

print(queue.dequeue())