# 2004: 조합 0의 개수
# 조합에서는 2와 5중 갯수가 더 작은게 10의 개수(짝이 맞아야 하니까)
# nCm일 때, 0의 갯수 = 
# (n!의 5의 갯수 - m!의 5의 갯수 - (n-m)!의 5의 갯수) 와
# (n!의 2의 갯수 - m!의 2의 갯수 - (n-m)!의 2의 갯수) 중에 더 작은 것

n,m = map(int,input().split())

def count_num(num,x): # (분석할 숫자,갯수 구할 숫자)
    cnt=0
    while num:
        num //= x
        cnt +=num
    return cnt

five_cnt = count_num(n,5) - count_num(m,5) - count_num(n-m,5) # n의 5의갯수 -m의 5의 갯수 - (n-m)의 5의 갯수
two_cnt = count_num(n,2) - count_num(m,2) - count_num(n-m,2)

res = min(five_cnt,two_cnt)
print(res)


