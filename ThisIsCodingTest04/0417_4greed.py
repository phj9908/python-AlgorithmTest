# 모험가 길드(최대한의 그룹 수를 만들기 위해 작은 공포도의 그룹부터 만들기,모든 모험가를 그룹에 넣지 않아도 됨)
n=int(input())
arr=sorted(list(map(int,input().split())))
answer=0
while len(arr)>0:
    p=arr[0]
    while p>0:
        arr.pop(0)
        p-=1
    answer+=1
print(answer)

         