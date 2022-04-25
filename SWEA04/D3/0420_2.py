# 13547. 팔씨름
tc=int(input())
for t in range(1,tc+1):
    str=input()
    cnt=0

    for s in str:
        if s=='x':
            cnt+=1
    if cnt>7:
        answer='NO'
    else:
        answer='YES'

    print(f'#{t} {answer}')