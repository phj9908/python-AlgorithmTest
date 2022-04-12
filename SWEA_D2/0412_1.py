# 1288. 새로운 불면증 치료법

tc= int(input())
for t in range(1,tc+1):
    n=int(input())

    arr=['0','1','2','3','4','5','6','7','8','9']
    k=1
    num_arr=[]
    while len(arr)>0:
        n*=k
        num_arr=list(set(str(n)))
        for i in num_arr:
            if i in arr:
                arr.remove(i)
        n//=k
        k+=1
        
    print(f'#{t} {(k-1)*n}')