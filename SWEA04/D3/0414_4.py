# 1216. [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin = open("input.txt", "r") 

def check(arr,len):
    res_length=0

    while len<101:
        for j in range(100-len+1):
            str=arr[j:j+len]
            if str==arr[j+len-1:j-1:-1]: # 회문인지 체크
                res_length=max(res_length,len)
        len+=1
    return res_length

for t in range(1,11):
    #tc=int(input())
    arr=[]
    for i in range(100):
        arr.append(list(sys.stdin.readline().strip()))
    answer=0

    for i in range(100):
        length=2
        res_length_col=check(arr[i],length) # 가로 체크

        str=''
        for j in range(100):
            str+=arr[j][i]  
        str=list(str)
        res_length_row=check(str,res_length_col) # 세로 체크

        answer=max(answer,res_length_col,res_length_row) 
    
    print(f'#{t} {answer}')
            
