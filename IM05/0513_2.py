# 2116 주사위 쌓기
import copy
import sys
sys.setrecursionlimit(10**6) # Python이 정한 최대 재귀 갚이를 변경/ 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행

def up_down_idx(idx):
    if idx==0:
        return 5
    if idx==1:
        return 3
    if idx==2:
        return 4
    if idx==3:
        return 1
    if idx==4:
        return 2
    if idx==5:
        return 0

def recur(num,arr,cnt,sum):
    global answer

    if cnt==n:
        answer=max(answer,sum)
        return

    reverse_idx=up_down_idx(arr[cnt].index(num)) # 반대면 숫자의  idx
    x=arr[cnt][reverse_idx]
    arr[cnt].remove(num)
    arr[cnt].remove(x)

    sum+=max(arr[cnt])
    recur(x,arr,cnt+1,sum)


n=int(input())
arr_list=[]
for i in range(n):
    arr_list.append(list(map(int,input().split())))
answer=0
for i in range(6):
    arr=copy.deepcopy(arr_list)
    recur(arr[0][i],arr,0,0) # 1번 주사위의 아랫면이 될 숫자, 배열, 주사위 갯수, 합
print(answer)


