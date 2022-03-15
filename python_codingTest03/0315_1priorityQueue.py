# 스택.pop()=맨 마지막거 추출 / 큐.pop()=맨 처음거 추출/ 우선순위 큐.pop()=우선순위 젤 높은거 추출
# https://www.youtube.com/watch?v=AjFlp951nz0 먼저 참고


# 내장 라이브러리 이용하여 오름자순 정렬(최소 힙)
import heapq

def heap_sort(arr): 
    my_heap=[]
    res=[]

    for i in arr: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(my_heap,i) 
    for i in range(3): # 힙에 삽입된 원소들 다시 차례대로 꺼내 담음
        res.append(heapq.heappop(my_heap))
    return res

num=[]
todo=[]
for _ in range(3):
    str=input()
    for i in str:
        if i==' ':
            num.append(int(str[:str.index(i)]))
            todo.append((int(str[:str.index(i)]),str[str.index(i)+1:]))
            break

num=heap_sort(num)
for i in num:
    for j in range(3):
        if todo[j][0]==i:
            print(todo[j][1])
