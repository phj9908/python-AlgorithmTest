# 11508 2+1세일
n=int(input())
price=[ int(input()) for i in range(n)]
price=sorted(price,reverse=True)
answer=0
for i in range(0,len(price),3):
    answer+=sum(price[i:i+2])
print(answer)
