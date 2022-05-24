#20207 달력 

n=int(input())
hash={}
start,end=366,0
for _ in range(n):
    s,e=map(int,input().split())
    for i in range(s,e+1):
        if i in hash.keys():
            hash[i]+=1
        else:
            hash[i]=1
    start=min(start,s) # 입력받으면서 입력값중에 최솟값 찾기
    end=max(end,e)
s=0
first=True
row=0
total=0
for i in range(start,end+2):
    if i in hash.keys():
        row=max(row,hash[i])
        if first:
            s=i # 한 써클 시작 인덱스
            first=False
    if i not in hash.keys():
        col=i-s
        total+=col*row
        first=True
        row=0

print(total)
