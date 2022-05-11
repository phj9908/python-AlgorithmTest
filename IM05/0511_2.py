# 2477 참외밭
from collections import deque

n=int(input())
arr=deque()
max_x,max_y=0,0
for _ in range(6):
    d, l = map(int, input().split())
    arr.append((d,l))
    if (d==3 or d==4) and max_x<l:
        max_x=l
    elif (d==1 or d==2) and max_y<l:
        max_y=l

answer=0
while 1:
    if arr[0][1] == max_x and arr[-1][1] == max_y:
        answer = ((arr[0][1] * arr[-1][1]) - (arr[2][1] * arr[3][1])) * n
        break
    elif arr[0][1] == max_x and arr[1][1] == max_y:
        answer = ((arr[0][1] * arr[1][1]) - (arr[4][1] * arr[3][1])) * n
        break
    arr.rotate(1)  # 맨 뒤의 원소를 맨 앞의 원소로 이동
    
print(answer)


