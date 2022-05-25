# 1942 디지털 시계

def fun(s,e):
    cnt=0
    i=s
    while i<e+1:
        if str(i)[-4:]=='6000':
            i+=4000
            continue
        if str(i)[-2:]=='60':
            i+=40
            continue
        if i % 3 == 0:
            cnt += 1
        i+=1
    return cnt

for _ in range(3):
    s,e=input().split()
    s=int(''.join(s.split(':')))
    e=int(''.join(e.split(':')))
    cnt = 0

    if s>e:
        cnt+=fun(s,235959)
        cnt+=fun(0,e)
        print(cnt)
        continue

    cnt+=fun(s,e)
    print(cnt)