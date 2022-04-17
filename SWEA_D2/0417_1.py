# 5356. 의석이의 세로로 말해요
tc= int(input())
for t in range(1,tc+1):
    length=0
    arr=[]
    for i in range(5):
        str=list(input())
        arr.append(str)
        length=max(len(str),length)

    answer=''
    for i in range(length):
        for j in range(5):
            try:
                answer+=arr[j][i]
            except:
                answer+=''

    print(f'#{t} {answer}')
