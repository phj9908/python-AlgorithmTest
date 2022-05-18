# 13305 주유소 ( 다시 풀어보기 )
n=int(input())
len_arr=list(map(int,input().split()))
price_arr=list(map(int,input().split()))

sum_price=price_arr[0]*len_arr[0] # 처음 도시는 무조건 그 지역의 기름값으로 계산
min_price=price_arr[0]

for i in range(1,len(price_arr)-1):
    if price_arr[i]<min_price:
        min_price=price_arr[i]
    sum_price+=min_price*len_arr[i]

print(sum_price)

