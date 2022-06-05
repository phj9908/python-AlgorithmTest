# 최소 직사각형
def solution(sizes):
    arr=[]
    for i in sizes:
        i=sorted(i)
        arr.append(i)
    arr=sorted(arr,key=lambda x: x[0],reverse=True)
    col=arr[0]
    arr=sorted(arr,key=lambda x: x[1],reverse=True)
    row=arr[0]

    return col[0]*row[1]
