# 만들수 없는 금액
import time
start_time=time.time()

n=int(input())
arr=list(map(int,input().split())) # 3 2 1 1 9

i=1
arr2=[]
while i<=len(arr):
    for j in range(len(arr)-(i-1)):
        arr2.append(sum(arr[j:j+i]))
    i+=1

k=1
while 1:
    if k not in arr2:
        break
    k+=1

print(k)
end_time=time.time()
print(f'time: {end_time-start_time}')        
