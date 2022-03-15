# 우선순위 큐 직접구현

MAX_SIZE_QUEUE=101

class Heap():
    def __init__(self):
        self.arr=[None]*MAX_SIZE_QUEUE
        self.heap_cnt=0
    
    def compare_with_parent(self,idx):
        if idx<=1:
            return False
        parent_idx=idx//2
        if self.arr[idx]<self.arr[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        self.heap_cnt+=1

        if self.heap_cnt==1:
            self.arr[self.heap_cnt]=data
            return
        self.arr[self.heap_cnt]=data
        insert_idx=self.heap_cnt

        while self.compare_with_parent(insert_idx):
            parent=insert_idx//2
            self.arr[insert_idx],self.arr[parent]=self.arr[parent],self.arr[insert_idx]
            insert_idx=parent
        return True

    def compare_with_child(self,idx):
        left=idx*2
        right=idx*2+1

        if self.arr[left]==None and self.arr[right]==None:
            return False
        if self.arr[right]==None:
            if self.arr[left]<self.arr[idx]:
                return left
            else:
                return False
        if self.arr[left]<self.arr[right]:
            return left
        else:
            return right

    def pop(self):
        idx=1
        root=self.arr[1]

        terminal_data=self.arr[self.heap_cnt]
        self.arr[self.heap_cnt]=None
        self.arr[idx]=terminal_data
        self.heap_cnt-=1

        while True:
            child_idx=self.compare_with_child(idx)
            if child_idx==False:
                break
            self.arr[child_idx],self.arr[idx]=self.arr[idx],self.arr[child_idx]
            idx=child_idx
        
        return root

def heap_sort(heap:Heap(),arr):
    my_heap=[]
    res=[]

    for i in arr:
        heap.insert(i)
    for _ in range(3):
        res.append(heap.pop())
    return res

num=[]
todo=[]
for _ in range(6):
    str=input() # 3 "abc"
    for i in str: 
        if i==' ':
            num.append(int(str[:str.index(i)])) # 3
            todo.append((int(str[:str.index(i)]),str[str.index(i)+1:])) # (3,"abc")
            break

heap=Heap()
num=heap_sort(heap,num)
cnt=0
for i in num:
    for j in range(len(todo)):
        if todo[j][0]==i:
            print(todo[j][1])  
            cnt+=1
        if cnt==3 : break