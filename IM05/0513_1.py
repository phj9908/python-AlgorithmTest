#2527 직사각형 (다시풀기)
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2=map(int,input().split())

    if p1<x2 or p2<x1 or y1>q2 or q1<y2:
        print('d')
        continue
    elif x1==p2 or x2==p1:
        if q1 == y2 or q2==y1:
            print('c')
        else:   # x축방향 면들이 접한 경우
            print('b')
    elif y1==q2 or q1==y2 : # y축 방향 면들이 접한 경우
        print('b')

    else:
        print('a')


