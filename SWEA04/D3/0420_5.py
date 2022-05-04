# 신뢰(다시풀어보기)
# https://colinder.github.io/sw_21.01.04/

tc=int(input())
for t in range(1,tc+1):
    arr=input().split()
    prev=''
    b_stack,o_stack=1,1
    b_time,b_total=0,0
    o_time,o_total=0,0
    total=0
    double_btn=False # 블랙,오렌지 버튼 둘 다 눌린 경우

    for i in arr[1:]: # arr[0]은 빼기
        if i.isalpha():
            if prev==i:
                double_btn=True
            else:
                double_btn=False
                prev=i
        elif prev=='B':
            if double_btn:
                b_time=abs(int(i)-b_stack)+1
            else:
                if o_total<=abs(int(i)-b_stack):
                    b_time=abs(int(i)-b_stack)-o_total+1
                else:
                    b_time=1
                o_total=0
            b_total+=b_time
            total+=b_time
            b_stack=int(i)
        else:
            if double_btn:
                o_time=abs(int(i)-o_stack)+1
            else:
                if b_total<=abs(int(i)-o_stack):
                    o_time=abs(int(i)-o_stack)-b_total+1
                else:
                    o_time=1
                b_total=0
            o_total+=o_time
            total+=o_time
            o_stack=int(i)

    print(f'#{t} {total}')        