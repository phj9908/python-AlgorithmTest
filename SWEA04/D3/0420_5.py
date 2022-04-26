# 신뢰(아직 못품)
# https://colinder.github.io/sw_21.01.04/
# 중복되는 시간 빼는 방법..?
tc=int(input())
for t in range(1,tc+1):
    arr=list(input().split())
    num=arr[0]
    del arr[0]
    b_stack=[1]
    o_stack=[1]
    b_time,b_total=0,0
    o_time,o_total=0,0

    while len(arr)!=0:
        
        x=arr.pop(0)
        n=int(arr.pop(0))
        if x=='B':
            b_time=abs(b_stack[-1]-n)+1
            b_total+=b_time
            if o_time<b_total:
                if o_total<b_total:
                    b_total-=o_total
                else:
                    b_total-=o_time
            b_stack.append(n)

        else:
            o_time=abs(o_stack[-1]-n)+1
            o_total+=o_time
            if b_time<o_total:
                if b_total<o_total:
                    o_total-=b_total
                else:
                    o_total-=b_time
            o_stack.append(n)
    
    print(f'#{t} {b_total+o_total}')     
    
        