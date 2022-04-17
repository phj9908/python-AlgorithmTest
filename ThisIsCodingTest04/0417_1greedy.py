# 거스름 돈 : 최대한 큰 단위로 나누기
n=1260
answer=0

arr=[500,100,50,10]
for i in arr:
    answer+=n//i
    n%=i
print(answer)