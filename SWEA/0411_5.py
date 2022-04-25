# 1204.최빈값 구하기
from collections import Counter

tc=int(input())
for t in range(1,tc+1):
    num=int(input())
    arr=Counter(list(input().split())).most_common()

    print(f'#{t} {arr[0][0]}')