#2669 직사각형 네개의 합집합의 면적 구하기
arr=[ [0]*101 for i in range(101)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            if arr[i][j]!=1:
                arr[i][j]=1
answer=0
for i in arr:
    answer+=i.count(1)
print(answer)
