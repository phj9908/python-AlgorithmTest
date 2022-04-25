# 1229. [S/W 문제해결 기본] 8일차 - 암호문2
for t in range(1,11):
    length=int(input())
    code=list(map(int,input().split()))
    com_num=int(input())
    command=list(input().split())

    for i in range(len(command)):
        if command[i]=='I':
            x=int(command[i+1])
            y=int(command[i+2])
            s=command[i+3:i+3+y]

            for j in range(y):
                code.insert(x+j,s[j])
        if command[i]=='D':
            x=int(command[i+1])
            y=int(command[i+2])

            for j in range(1,y+1):
                del(code[x]) # 어차피 del[x]하면 그자리에 x+1원소가 들어가니 code[x+j]가 아니고 code[x]가 맞음!

    print(f'#{t}',end=' ');print(*code[:10])