# 1859 백만장자 프로젝트(다시풀어보기)
# 문제이해 https://itcrowd2016.tistory.com/87

tc=int(input())
for t in range(1,tc+1):
    n= int(input())
    nums= list(map(int,input().split()))
    sum=0
    if nums.index(max(nums))!=0:  # 가장 큰 값이 0인덱스면 아무것도 안사는것이 최대이익이기에 답은 0
        max_p=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if max_p<nums[i]:
                max_p=nums[i]
            else:
                sum+=max_p-nums[i]
             
    print(f'#{t}',end=' ');print(sum)

#내가 생각한 풀이 (확인은 안함)
# answer=0
# stack=[]
# if arr.index(max(arr))==0:
#     print(0)
#     exit()
# for i in range(len(arr)):
#     if stack[-1]<arr[i]:
#         while stack:
#             answer+=arr[i]-stack.pop()
#         continue
#     stack.append(arr[i])
#