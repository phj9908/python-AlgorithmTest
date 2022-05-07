# 2605 줄세우기

n=int(input())
arr=list(map(int,input().split()))
answer=[]
for i,v in enumerate(arr):
    answer.insert(v,i+1)
answer=reversed(answer)
print(*answer)


