from re import A
from typing import Counter


#3456. 직사각형 길이 찾기
tc=int(input())
for t in range(1,tc+1):
    arr=list(map(int,input().split()))
    
    if arr[0]==arr[1]==arr[2]:
        answer=arr[0]
    else:
        answer=Counter(arr).most_common()[1][0]
    
    print(f'{t} {answer}')
