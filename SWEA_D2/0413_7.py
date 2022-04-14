#1234. [S/W 문제해결 기본] 10일차 - 비밀번호

def check(num):
    for i in range(len(num)-1):
        if nums[i]==nums[i+1]:
            return False
    return True

for t in range(1,11):
    n, nums=input().split()
    n=int(n)
    nums=list(nums)
    i=0

    while 1:
        # # 다른방법
        # if nums[i] ==nums[i+1]:
        #     del(nums[i:i+2])
        #     n-=2
        #     i-=2
        # i+=1
        # if i==n-1:
        #     break
        if nums[i]==nums[i+1]:
            nums=nums[:i]+nums[i+2:]
        if check(nums):
            answer=nums
            break
        i=(i+1)%(len(nums)-1)

    print(f'#{t}',end=' ')
    for i in answer:
        print(i,end='')
    print()
