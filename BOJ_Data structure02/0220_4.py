#1406 에디터
import sys

pop_arr=[] # 커서 기준 오른쪽에 있는 문자열
arr = list(sys.stdin.readline().strip())  # sys.stdin.readline의 입력에 stack기능 쓸려면 list()감싸주기 , 커서 기준 왼쪽에 있는 문자열
m = int(sys.stdin.readline())
 
for i in range(m):
    str = sys.stdin.readline().split()
    if  str[0] == 'P' :
        arr.append(str[1])  
         
    if str[0] == 'L' :
            if arr : # len(arr) !=0
                pop_arr.append(arr.pop()) 
             
    if str[0] == 'D'   :
            if pop_arr: # len(pop_arr) !=0
                arr.append(pop_arr.pop())
             
    if str[0] == 'B' :
            if arr :
                arr.pop()
arr.extend(reversed(pop_arr)) # reverse()는 리스트에 값이 없으면 err. reversed 써야함.
print(''.join(arr))  

