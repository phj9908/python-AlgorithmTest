#6550 부분문자열( 다시풀기 )
# 입력 테케가 여러개있다고만 하면 while 1: try~except:break 로 감싸기
while 1:
    try:
        s,t =input().split()
        answer=False

        cnt=0
        for i in range(len(t)):
            if t[i]==s[cnt]:
                cnt+=1
                if cnt==len(s):
                    answer=True
                    break
        if answer:
            print('Yes')
        else:
            print('No')

    except:
        break




