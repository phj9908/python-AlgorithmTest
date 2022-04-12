# 1230 암호문 3 (다시 풀어보기)
for t in range(1, 11) :
    length=int(input())
    word=list(map(int,input().split()))
    com_num=int(input())
    command=list(input().split())
    
    for i in range(len(command)):
        if command[i]=='I': #  I 3 2 123152 487651 
            x=int(command[i+1]) # 3
            y=int(command[i+2]) # 2
            s=command[i+3:]     # 123152 487651 
            for j in range(y):
                word.insert(x+j,s[j]) # 인덱스 x+j에 s[j]추가
        if command[i]=='D':
            x=int(command[i+1])
            y=int(command[i+2])
            for j in range(1,y+1):
                del(word[x+j])
        if command[i]=='A':
            y=int(command[i+1])
            s=command[i+2:]
            for j in range(y):
            	word.append(s[j])
    
    # print(f'#{t}',end=' ')
    # print(*word[:10])

