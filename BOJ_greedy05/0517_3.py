# 8980 택배 (다시풀기 ,해시로 풀었지만 반만 맞음)
# https://hillier.tistory.com/105
n,weight=map(int,input().split()) # 마을 수, 트럭 용량
m=int(input()) # 박스 갯수
arr=[list(map(int,input().split())) for i in range(m)]
arr=sorted(arr,key=lambda x:x[1]) # 빠른 도착점 기준으로 정렬

box=[weight]*n # 각 마을에서 기록할 박스용량
total=0
for a,b,c in arr:
    _min=weight
    for i in range(a,b):
        _min=min(_min,box[i])
    _min=min(_min,c) # 감량할 최소 박스 용량
    for i in range(a,b):
        box[i]-=_min # 마을마다 박스 용량 감량
    total+=_min # 지금까지 뺐던 박스 용량
print(total)






