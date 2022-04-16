# 5515. 2016년 요일 맞추기
tc= int(input())
arr={0:0,1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for t in range(1,tc+1):
    m,d = map(int,input().split())
    answer=0
    if m==1 and d<=3:
        answer=3+d
    elif m==1 and d>3 and d<11:
        answer=d-4
    else:
        i=1
        while 1:
            m-=1
            d+=arr[m]
            if m<=0:
                break
        answer=(d-4)%7
    
    print(f'#{t} {answer}')


        

