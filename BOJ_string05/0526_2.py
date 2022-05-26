# 4659 비밀번호 발음하기
moum='aeiou'
while 1:
    pw=input()
    if pw=='end':
        break

    for m in moum:
        if m in pw:
            break
    else:
        print(f'<{pw}> is not acceptable.')
        continue

    m_cnt,j_cnt=0,0
    err=False
    for i in pw:
        if i in moum:
            m_cnt+=1
            j_cnt=0
            if m_cnt>=3:
                err=True
        if i not in moum:
            j_cnt+=1
            m_cnt=0
            if j_cnt>=3:
                err=True

    if err:
        print(f'<{pw}> is not acceptable.')
        continue
    else:
        for i in range(len(pw)-1):
            if pw[i]==pw[i+1]:
                if pw[i]=='e' or pw[i]=='o':
                    continue
                else:
                    print(f'<{pw}> is not acceptable.')
                    break
        else:
            print(f'<{pw}> is acceptable.')








