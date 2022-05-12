#2628 종이 자르기( 다시풀어보기 )
r,c = map(int,input().split())
row=[0,r] #[0,8]
col=[0,c] #[0,10]
num=int(input())
for _ in range(num):
    d, l = map(int,input().split())
    if d==1: 
        row.append(l)
    else:
        col.append(l)
row.sort() # [0,2,3,8]
col.sort() # [0,4,10]

answer_r=[]
answer_c=[]
for i in range(len(row)-1):
    answer_r.append(row[i+1]-row[i])
for i in range(len(col)-1):
    answer_c.append(col[i+1]-col[i])
print(max(answer_r)*max(answer_c))

