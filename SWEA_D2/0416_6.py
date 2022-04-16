# 13229. 일요일
tc= int(input())
arr={'MON':6,'TUE':5,'WED':4,'THU':3,'FRI':2,'SAT':1,'SUN':7}
for t in range(1,tc+1):
    word=input()
    print(f'#{t} {arr[word]}')