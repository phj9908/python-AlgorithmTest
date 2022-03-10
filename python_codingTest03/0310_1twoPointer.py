#슬라이딩 윈도우
# two pointer 와 달리 두 개의 포인터를 사용하지 않고 고정된 크기의 부분만 확인

num=[]
t_c=[]
caf=[]
tau=[]

for _ in range(10):
    n, c, t = map(int,input().split())
    num.append(n)
    caf.append(c)
    tau.append(t)
    t_c.append(t-c)

start=0
partial_sum=0
res_idx=0

while start<= 6:
    if partial_sum <sum(t_c[start:start+3]):
        partial_sum=sum(t_c[start:start+3])
        res_idx=start
    start+=1
    
print(f'{res_idx} {res_idx+1} {res_idx+2}의 타우린 합은 {sum(tau[start:start+3])}, 카페인 합은 {sum(caf[start:start+3])}로 가장 효과가 좋습니다.')
    

    