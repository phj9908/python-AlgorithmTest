# 4371. 항구에 들어오는 배 (다시풀어보기)
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    arr=[]
    
    for i in range(n):
        arr.append(int(input()))
    arr_set=set()

    cnt=0
    for i in range(1,len(arr)):
        if arr[i] in arr_set:
            continue

        gap=arr[i]-1
        for j in range(arr[i],arr[-1]+1,gap): # 에라토스테네스의 ㅇ체와 빗스한 알고리즘, 배수를 미리 알아둔다
            arr_set.add(j)
        cnt+=1

    print(f'#{t} {cnt}')