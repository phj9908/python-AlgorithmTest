# 10973 이전 순열
# 다음 순열에서 부등호방향 반대로 + swap인덱스 뒤 내림차순 정렬
import sys

n=int(input())
num=list(map(int,input().split()))
swap=0

for i in range(len(num)-1,0,-1): 
    if num[i-1]>num[i]: # 뒤칸보다 앞칸이 클 때
        swap=i-1
        break
else: # 오름차순인 경우
    print(-1)
    sys.exit()

for i in range(len(num)-1,0,-1): 
    if num[swap]>num[i]: # swap칸 보다 작은 원소있다면
        num[swap],num[i]=num[i],num[swap] # swap
        num= num[:swap+1]+sorted(num[swap+1:],reverse=True)# swap인덱스 뒤는 내림차순 정렬

        print(*num)
        break
