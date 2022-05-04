for t in range(1,int(input())+1):
    arr=input().split()
    prev=''
    b_stack,o_stack=1,1
    b_time,o_time,b_total,o_total=0,0,0,0
    total=0
    double_btn=False

    for i in arr[1:]:
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
                if o_total<abs(int(i)-b_stack):
                    b_time=abs(int(i)-b_stack)-o_total+1
                else:
                    b_time=1

