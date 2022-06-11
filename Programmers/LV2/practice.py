def solution(rows,columns,queries):
    answer=[]
    arr=[ [0]*(columns+1) for i in range(rows+1)]

    x=1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j]=x
            x+=1

    for y1,x1,y2,x2 in queries:
        tmp=arr[y1][x1]
        _min=tmp

        for k in range(y1,y2):
            t=arr[k+1][x1]
            arr[k][x1]=t
            _min=min(_min,t)

        for k in range(x1,x2):
            t=arr[y2][k+1]
            arr[y2][k]=t
            _min=min(_min,t)

        for k in range(y2,y1,-1):
            t=arr[k-1][x2]
            arr[k][x2]=t
            _min=min(_min,t)

        for k in range(x2,x1,-1):
            t=arr[y1][k-1]
            arr[y1][k]=t
            _min=min(_min,t)

        arr[y1][x1+1]=tmp
        answer.append(_min)

    return answer


