# #1234. [S/W 문제해결 기본] 10일차 - 비밀번호

for t in range(1,11):
    n,pw=input().split()
    n=int(n)
    pw=list(pw)
    while 1:
        for i in range(len(pw)-1):
            if pw[i]==pw[i+1]:
                del pw[i:i+2]
                break
        else:
            break
    pw=''.join(pw)
    print(f'#{t} {pw}')

