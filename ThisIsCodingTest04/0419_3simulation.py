# 왕실의 나이트
arr={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
start= input()
x=arr[start[0]]
y=int(start[-1])

dx=[-2,-2,2,2,1,-1,1,-1]
dy=[1,-1,1,-1,-2,2,-2,2]

answer=0
for i in range(8):
    if x+dx[i]<0 or x+dx[i]>=8 or y+dy[i]<0 or y+dy[i]>=8:
        continue
    answer+=1
print(answer)

