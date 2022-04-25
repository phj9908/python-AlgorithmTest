# 1984 중간 평균값 구하기

tc=int(input())
for t in range(1,tc+1):
    nums=list(map(int,input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    answer=round(sum(nums)/len(nums))
    print(f'#{t} {answer}')