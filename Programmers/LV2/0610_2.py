# 행렬 테두리 회전하기( 두가지 방법으로 풀기 )

# https://minnit-develop.tistory.com/23 참고
def solution(rows,columns,queries):

    answer=[]
    arr=[ [0]*(columns+1) for i in range(rows+1)]
    x=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j]=x
            x+=1

    for y1,x1,y2,x2 in queries:
        tmp=arr[y1][x1] # 미리 저장한뒤 나중에 맞는 자리에 할당
        _min=tmp

        # 왼쪽 세로 -> 하단 가로 -> 오른쪽 세로 -> 상단 가로 순서로 정렬!
        # 원소간에 스왑하는 순서도 반시계 방향으로 탐색!
        for k in range(y1,y2): # 왼쪽 세로줄 (y2는 하단 가로줄에서 처리 예정)
            t=arr[k+1][x1]
            arr[k][x1]=t
            _min=min(_min,t)
        print(arr)

        for k in range(x1,x2): # 하단 가로줄(x1...
            t=arr[y2][k+1]
            arr[y2][k]=t
            _min=min(_min,t)
        print(arr)

        for k in range(y2,y1,-1): # 오른쪽 세로줄 (y1...
            t=arr[k-1][x2]
            arr[k][x2]=t
            _min=min(_min,t)
        print(arr)

        for k in range(x2,x1,-1): # 상단 가로줄 (x1는 오른쪽 세로줄에서 처리)
            t=arr[y1][k-1]
            arr[y1][k]=t
            _min=min(_min,t)
        print(arr)

        arr[y1][x1+1]=tmp # arr[y1][x1]의 시계방향 한 칸 이동한 자리
        answer.append(_min)

    return answer

# deque.rotate() ver , 시계방향으로 탐색
from collections import deque
def solution2(rows,columns,queries):
    arr=[ [0]*(columns+1) for i in range(rows+1)]
    x=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j]=x
            x+=1
    queue,answer=deque(),[]

    for y1,x1,y2,x2 in queries:
        for x in range(x2-x1):
            queue.append(arr[y1][x1+x])
        for y in range(y2-y1):
            queue.append(arr[y2+y][x2])
        for x in range(x2-x1):
            queue.append(arr[y2][x2-x])
        for y in range(y2-y1):
            queue.append(arr[y2-y][x1])

        queue.rotate(1)
        answer.append(min(queue))

        for x in range(x2-x1):
            arr[y1][x1+x]=queue.popleft()
        for y in range(y2-y1):
            arr[y1+y][x2]=queue.popleft()
        for x in range(x2-x1):
            arr[y2][x2-x]=queue.popleft()
        for y in range(y2-y1):
            arr[y2-y][x1]=queue.popleft()

        return answer



