# 배열의 단점
# 배열의 3번째 인덱스를 빼는 스레드와 배열을 출력하는 스레드 동시에 실행
#하면 오류가 생김!

from threading import Thread
import time

arr=[0,1,2,3,4]

def delete_fun(idx):
    global arr
    time.sleep(1) # 1ms 딜레이

    arr=arr[0:idx]+arr[idx+1:] # 특정 인덱스 제외하기

def print_fun():
    global arr
    len = len(arr)
    time.sleep(2) #2ms딜레이 -> 위의 delete함수 보다 1ms뒤에 실행. 

    for i in range(len):
        print(arr[i]) # 위에서 삭제된 인덱스로 인해 오류발생

# 스레드 생성
th1 = Thread(target=delete_fun,arg=(3,)) # Thread(실행하려는 함수,그 함 수의 매개변수)
th2 = Thread(target=print_fun,args=())

# 스레드 동시 실핼
th1.start()
th2.start()