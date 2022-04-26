# 모험가 길드(최대한의 그룹 수를 만들기 위해 작은 공포도의 그룹부터 만들기,모든 모험가를 그룹에 넣지 않아도 됨)
n=int(input())
arr=sorted(list(map(int,input().split())))
answer=0
cnt=0
for i in arr:
    cnt+=1
    if cnt>=i:
        answer+=1
        cnt+=1
print(answer)

         