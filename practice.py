for t in range(1,int(input())+1):
    n=int(input())
    hash={}
    cnt,start=0,0
    answer=False
    check=0
    zero=False

    for i in range(n):
        arr=list(map(int,input().split()))
        if arr[0] == 0:
            hash[i + 1] = [arr[0]]
            check += 1
            zero = True
        else:
            if arr[0]>=2:
                hash[i+1]=[]
                for j in range(1,arr[0]+1):
                    hash[i + 1].append(arr[j])
                    check += 1
            else:
                hash[i+1]=[arr[1]]
                check+=1

    if not zero:
        cnt=-1
        print(f'#{t} {cnt}')
        continue

    try:
        while 1:
            cnt+=1
            for k,v in hash.items():
                if start in v:
                    if len(v)==1:
                        start=k
                        v.remove(start)
                        check-=1
                        if check==0:
                            answer=True
                            break

            else:
                continue
            break
    except:
        cnt = -1
        print(f'#{t} {cnt}')

    if answer:
        print(f'#{t} {cnt}')



















