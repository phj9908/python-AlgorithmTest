# 큐를 제대로 쓴 코드는 아닌 것 같음...일단 보류

import queue

id_arr=[]
time_arr=[]

for i in range(7):
    id, time= map(int,input().split())
    id_arr.append(id)
    time_arr.append(time)

queue=[]
head=-1
break_cnt=0
sum_time=0

while head<len(time_arr)-1:
    
    if sum(queue)<50:
        head+=1
        queue.append(time_arr[head])
        if head==len(time_arr)-1:
            sum_time+=sum(queue)
            for _ in range(len(queue)):
                print(id_arr[time_arr.index(queue.pop())],end=', ')
            print()
    
    if sum(queue)==50:
        sum_time+=sum(queue)
        for _ in range(len(queue)):
            print(id_arr[time_arr.index(queue.pop())],end=', ') # join은 리스트가 입력변수라서 그거 말고 다른 출력 방법??
        print()
        break_cnt+=1
    
    if sum(queue)>50:
        queue.pop()
        sum_time+=sum(queue)
        
        for _ in range(len(queue)):
            print(id_arr[time_arr.index(queue.pop())],end=', ')
        print()
        break_cnt+=1
        head-=1

print(f'총 소요시간: {sum_time+break_cnt*10}분')
        



