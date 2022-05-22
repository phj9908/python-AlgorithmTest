# 20546 기적의 매매법

coin=int(input())
arr=list(map(int,input().split()))
a_ans,b_ans=coin,coin

total_cnt=0
for i in range(len(arr)):
    if a_ans<arr[i]:
        continue
    cnt=a_ans//arr[i]
    a_ans%=arr[i]
    total_cnt+=cnt
    if a_ans==0:
        break
a_ans+=arr[-1]*total_cnt

total_cnt=0
for i in range(len(arr)-3):
    if total_cnt and arr[i]<arr[i+1]<arr[i+2]:
        b_ans=total_cnt*arr[i+3]
        total_cnt=0
    elif arr[i]>arr[i+1]>arr[i+2]:
        total_cnt+=b_ans//arr[i+3]
        b_ans%=arr[i+3]
b_ans+=arr[-1]*total_cnt

if a_ans>b_ans:
    print('BNP',a_ans,b_ans)
elif a_ans<b_ans:
    print('TIMING',a_ans,b_ans)
else:
    print('SAMESAME')

