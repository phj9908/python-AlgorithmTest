# 완전 이진 트리 <- 배열 이용 / 이진 트리 <- 링크드 리스트 이용 
# 완전이진트리는 무조건 왼쪽 자식노드 부터 채움
# 최상단 노드가 배열의 1번 인덱스라하면
# 그 왼쪽 자식노드는 2번, 오른쪽 자식노드는 3번이 됨으로써
# 왼쪽 자식노드 인덱스=부모 노드 인덱스*2 / 오른쪽 자식노드 = 부모 노드 인덱스*2 +1
# 힙의 두 종류
# 부모노드가 항상 자식노드보다 작은 완전이진 트리형태(최소 힙) or 
#                            큰                   (최대 힙)  
# 힙은 데이터 삭제시 루트노드만 추출함(최상단 노드), 그자리를 맨 마지막 인덱스 노드로 스왑하고 자식노드랑 크기비교해 가면서 다시 정렬...

# 최소 힙 구현(자식이 부모보다 크다)

MAX_HEAP_SIZE=101

class Heap():    # 힙 선언
    def __init__(self): # 무조건 왼쪽부터 채우기에 self.left, self.right 필요 X 그냥 self.arr[idx]에 할당
        self.arr=[None]*MAX_HEAP_SIZE
        self.heap_cnt=0

    def compare_with_parent(self,idx): # 부모노드와 크기비교(데이터 삽입시 사용)
        if idx<=1:
            return False # 최상단 노드니까 비교할 필요X
        parent_idx=idx//2
        if self.arr[idx]< self.arr[parent_idx]: # 부모노드 값이 더 크냐
            return True
        else:
            return False

    def insert(self,data):
        self.heap_cnt+=1

        if self.heap_cnt==1:
            self.arr[self.heap_cnt]=data
            return

        self.arr[self.heap_cnt]=data # 일단 마지막 노드에 추가
        insert_idx = self.heap_cnt

        while self.compare_with_parent(insert_idx): # 부모노드 값이 더 크면
            parent = insert_idx//2
            self.arr[insert_idx],self.arr[parent]=self.arr[parent],self.arr[insert_idx] # 스왑
            insert_idx = parent
            #print(self.arr[1:self.heap_cnt+1])
        return True

    def compare_with_child(self,idx): # 자삭노드랑 크기비교를 할 필요가 있냐
        left=2*idx
        right=2*idx+1

        if self.arr[left]==None and self.arr[right]==None: # 최하단에 도착했을 때
            return False
        if self.arr[right]==None: # 오른쪽 자식노드가 없는 경우는 있지만 왼쪽 노드는 항상 있기에
            if self.arr[left]<self.arr[idx]:
                return left
            else:
                return False
        if self.arr[left]<self.arr[right]:
            return left
        else:
            return right
    
    def pop(self): # 최소힙이기에 루트 노드 추출(인덱스1 원소 추출)
        idx=1
        root=self.arr[1]

        terminal_data=self.arr[self.heap_cnt] # 루트노드 자리에 들어올 맨 마지막 원소값
        self.arr[self.heap_cnt]=None # 맨 마지막 노드 삭제
        self.arr[idx]=terminal_data 
        self.heap_cnt-=1

        while True:
            child_idx=self.compare_with_child(idx) # 자식노드들과 크기비교
            if child_idx==False: # = if not child_idx
                break
            self.arr[child_idx],self.arr[idx]=self.arr[idx],self.arr[child_idx]
            idx=child_idx
        
        return root

heap=Heap()
heap.insert(1)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(9)
heap.insert(10)
heap.insert(11)

print(heap.arr[1:heap.heap_cnt+1])
print(heap.pop())
print(heap.arr[1:heap.heap_cnt+1])
