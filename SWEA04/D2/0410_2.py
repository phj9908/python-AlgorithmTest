# 날짜 계산기

tc=int(input())
arr={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for t in range(1,tc+1):
    answer=0
    m1,d1,m2,d2 = map(int,input().split())
    if m1==m2:
        answer=d2-d1+1
    else:
        answer+=arr[m1]-d1+1
        while m1<m2-1:
            m1+=1
            answer+=arr[m1]
        answer+=d2
    print(f'#{t} {answer}')