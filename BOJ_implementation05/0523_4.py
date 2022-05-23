# 10994 변찍기-19(맞았지만 다시 풀어보기)
import copy

n=int(input())
number = 1 + 4 * (n - 1)
num=copy.deepcopy(number)
arr=[[] for i in range(num)]
start=0
while num>0:
    for i in range(number):
        if i==start or i==(number-1)-start:
            arr[i][start:-start]=['*']*num
        elif start<i<(number-1)-start:
            arr[i][start:-start]=['*']+[' ']*(num-2)+['*']
    start+=2
    num-=4
for i in arr:
    print(''.join(i))