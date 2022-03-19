MAX_QUEUE_SIZE=8

class Queue:
    def __init__(self):
        self.arr=[None]*MAX_QUEUE_SIZE
        self.head=0
        self.tail=0

    def is_empty(self):
        if self.head==self.tail:
            return True
        return False

    def is_full(self):
        if self.tail>=MAX_QUEUE_SIZE-1:
            return True
        return False

    def enqueue(self,data):
        if self.is_full():
            print('큐가 꽉 찼습니다.')
            return 
        self.tail=(self.tail+1)%MAX_QUEUE_SIZE
        self.arr[self.tail]=data

    def dequeue(self):
        if self.is_empty():
            print('큐가 이미 비었습니다.')
            return
        self.head=(self.head+1)%MAX_QUEUE_SIZE
        return self.arr[self.head]

queue=Queue()
for i in range(7):
    id, time= map(int,input().split())
    queue.enqueue((id,time))

break_cnt=0
sum_time=0
current_time=0
id_arr=[]

while not queue.is_empty():
    id, time = queue.dequeue()
    sum_time += time

    if current_time+time>50:
        print(id_arr) # 그때까지 저장된 배열 출력
        id_arr=[id]   # 저장됐던 아이디들 없애고 새로 저장
        current_time=time  
        break_cnt+=1

    else:
        current_time+=time
        id_arr.append(id)

print(id_arr) # 마지막 배열 출력
print(f'총 소요시간: { sum_time+break_cnt*10}분')
        



