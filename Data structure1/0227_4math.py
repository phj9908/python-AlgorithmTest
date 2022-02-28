# 11576 Base conversion : a진법을 B진법으로 변환

a,b = map(int,input().split())
n = int(input())
a_num=list(map(int,input().split()))
ten_num=0
res=[] # res를 문자열로 하고 추가한느 식이면 틀렸다고 뜸

pow=0
for i in a_num[::-1]: # 십진수로 변환
    ten_num+=i*(a**pow)
    pow+=1

while ten_num:
    res.append(str(ten_num%b))
    ten_num//=b
print(*res[::-1])
