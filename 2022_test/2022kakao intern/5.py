from collections import deque

def shiftRow(rc):
    arr=[]
    i=-1
    while i<2:
        arr.append(rc[i])
        i+=1
    return arr

d=[(0,1),(1,0),(0,-1),(-1,0)]
def rotate(rc,n,m):
    y,x=0,0
    arr=deque()
    arr.append(rc[0][0])
    dir=0
    while 1:
        y+=d[dir][0]
        x+=d[dir][1]
        if y<0 or y>n-1 or x<0 or x>m-1:
            y-=d[dir][0]
            x-=d[dir][1]
            dir+=1
            if dir==4:
                break
        else:
            arr.append(rc[y][x])
    arr.pop()
    arr.rotate(1)

    dir=0
    rc[0][0]=arr.popleft()
    while arr:
        y+=d[dir][0]
        x+=d[dir][1]
        if y<0 or y>n-1 or x<0 or x>m-1:
            y-=d[dir][0]
            x-=d[dir][1]
            dir+=1
        else:
            rc[y][x]=arr.popleft()

    return rc


def solution(rc, operations):

    for o in operations:
        if o=='Rotate':
            n,m=0,0
            n=len(rc)
            for _ in range(len(rc[0])):
               m+=1
            rc=rotate(rc,n,m)
        if o=='ShiftRow':
            rc = shiftRow(rc)
    return rc

solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"])