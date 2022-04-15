# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
for t in range(1,11):
    length=int(input())
    code=list(map(int,input().split()))
    num=int(input())
    command=list(input().split())

    for i in range(len(command)):
        if command[i]=='I':
            x=int(command[i+1])
            y=int(command[i+2])
            s=command[i+3:i+3+y]
            for j in range(y):
            	code.insert(x+j,s[j])
    #print(f'#{t}',end=' ');print(*code[:10])
