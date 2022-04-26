# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
import sys
sys.stdin = open("input.txt")

tc=1
nums=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

for t in range(1,tc+1):
    n,m =16,80
    arr=[]
    for i in range(n):
        arr.append(list(sys.stdin.readline().strip()))
    start_row=0
    start=0
    end=0
    code_arr=[]

    for i in range(len(arr)):
        if '1' in arr[i]:       # 암호 시작 줄 및 암호 구간 도출
            for j in range(m-1,-1,-1):
                if arr[i][j]=='1':
                    end=j
                    start=j-56+1
                    start_row=i
                    break
            break
        
    for i in range(start,end+1,7):
        str=arr[start_row][i:i+7]
        code_arr.append(nums.index(''.join(arr[start_row][i:i+7])))

    sum_1=0    
    sum_2=0
    for i in range(len(code_arr)):
        if (i+1)%2!=0:
            sum_1+=code_arr[i]
        elif (i+1)%2==0:
            sum_2+=code_arr[i]
    answer= (sum_1)*3+sum_2
    if answer%10!=0:
        answer=0
    else:
        answer=sum_1+sum_2

    print(f'#{t} {answer}')



