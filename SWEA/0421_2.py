# 12004. 구구단 1
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    for i in range(1,10):
        if n%i==0 and n//i<10:
            answer='Yes'
            break
        else:
            answer='No'
    print(f'#{t} {answer}')