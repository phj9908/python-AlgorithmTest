# 14696 딱지놀이
def check(a_arr,b_arr):
    if a_arr.count(4)>b_arr.count(4):
        return 'A'
    elif a_arr.count(4)<b_arr.count(4):
        return 'B'

    else:
        if a_arr.count(3) > b_arr.count(3):
            return 'A'
        elif a_arr.count(3) < b_arr.count(3):
            return 'B'
        else:
            if a_arr.count(2) > b_arr.count(2):
                return 'A'
            elif a_arr.count(2) < b_arr.count(2):
                return 'B'
            else:
                if a_arr.count(1) > b_arr.count(1):
                    return 'A'
                elif a_arr.count(1) < b_arr.count(1):
                    return 'B'
    return 'D'

n=int(input())
for i in range(n):
    a_arr=list(map(int,input().split()))
    b_arr=list(map(int,input().split()))

    print(check(a_arr[1:],b_arr[1:]))


