# 5986. 새샘이와 세 소수 (다시풀어보기)
# dfs로 하려니 중복되는 조합을 확인하기 어려움 (2,2,3)/(2,3,2)등등
# 아래처럼 3중 for문으로 하면 (2,2,3) (2,3,4)등 오름차순으로만 조합이 됨!

num=1000
sieve=[]
for i in range(2,num): # 소수로만 이뤄진 sieve 만들기
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        sieve.append(i)

tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    m=len(sieve)
    cnt=0
    for i in range(m): 
        if sieve[i]>n:
            break
        for j in range(i,m):
            if sieve[j]>n:
               break
            for k in range(j,m):
                if sieve[k]>n:
                    break
                if sieve[i]+sieve[j]+sieve[k]==n:
                    cnt+=1
    
    print(f'#{t} {cnt}')