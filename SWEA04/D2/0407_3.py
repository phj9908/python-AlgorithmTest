# 2007 패턴 마디의 길이 : 반복 문자열의 길이 반환
# KOREAKOREAKOREA..

tc=int(input())
for t in range(1,tc+1):
    s= input()
    cnt=0
    while 1:
        cnt+=1
        if s[:cnt]==s[cnt:cnt*2]:break
        
    print(f'#{t}',end=' ');print(cnt)
    