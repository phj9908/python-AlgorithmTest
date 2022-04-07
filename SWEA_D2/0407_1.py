# 1859 백만장자 프로젝트
# 문제이해 https://itcrowd2016.tistory.com/87

tc=int(input())
for t in range(1,tc+1):
    n= int(input())
    nums= list(map(int,input().split()))
    sum=0
    if nums.index(max(nums))!=0:          
        max_p=nums[-1]
        for i in range(len(nums)-1,-1,-1):
 
            if max_p<nums[i]:
                max_p=nums[i]
            else:
                sum+=max_p-nums[i]
             
    print(f'#{t}',end=' ');print(sum)