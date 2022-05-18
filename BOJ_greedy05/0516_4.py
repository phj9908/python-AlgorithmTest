# 2141 우체국 (다시풀기 )
# 인구의 절반이 속한 마을에 우체국 설치하기
import math

n=int(input())
arr=[ list(map(int,input().split())) for i in range(n)]
arr.sort() # x[0]기준으로 정렬
people_sum=0
for i,p in arr: # 인구수 누적합
    people_sum+=p
mid_p=math.ceil(people_sum/2) # 인구수의 중간 값
sum=0
for i,v in arr:
    sum+=v
    if sum>=mid_p: # 중간값을 넘을 때
        print(i)
        break
