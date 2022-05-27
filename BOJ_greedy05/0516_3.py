# 1092 배 (다시풀기, pypy3)

n=int(input()) # 크레인
limit_weight=list(map(int,input().split()))
m=int(input()) # 박스
weight=list(map(int,input().split()))
limit_weight=sorted(limit_weight,reverse=True)
weight=sorted(weight,reverse=True)
answer=0
if weight[0]>limit_weight[0]:
    print(-1)
    exit()
while weight:
    answer+=1
    for i in limit_weight:
        for j in weight:
            if i>=j:
                weight.remove(j)
                break       # 반복문 쓰면서 리스트 삭제할 때 , 이처럼 이중 for문해서 삭제할때마다 break
        if len(weight)==0:
            print(answer)
            exit()
# ex) 무게제한 = [ 9,8,5 ]
#     박스 무게 = [9,8,6,5] 이면 첫 1분 동안 무게 9,8,5옮길수 있게끔 1분마다 각 크레인 마다 옮길 박스 하나씩 찾아야함
