n = int(input())
time=[]

for i in range(n):
    (x,y) = map(int,input().split())
    time.append((x,y))
time=time.sort(key=lambda x:(x[1],x[0]))  # 종료시간 기준으로 먼저 오름차순, 같으면 시작시간 기준으로 오름차순

end_time,cnt=0

for start,end in time:
    if start>=end_time:
        cnt+=1
        end_time=end
print(cnt)


    
