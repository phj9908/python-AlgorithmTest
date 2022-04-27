# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 (다시풀기)
# dfs로 백트래킹 가지치기

def dfs(idx,cnt): # 인덱스, 교환한 횟수
    global answer
    if cnt==int(target):
        answer=max(int(''.join(nums)))
        return
    for now in range(idx,len(nums)):
        for max_idx in range(now+1,len(nums)):
            if nums[now]<=nums[max_idx]:
                nums[now],nums[max_idx]=nums[max_idx],nums[now]
                dfs(now,cnt+1)
                nums[now],nums[max_idx]=nums[max_idx],nums[now]

    if not answer and  cnt<int(target): # 이미 내림차순 정렬이 됐는데 교환 횟수가 남았을 때
        rotate=(int(target)-cnt)%2 
        if rotate:  # 남은 횟수가 홀수면 맨뒤 두개 교환(짝수면 그대로 반환)
            nums[-1],nums[-2]=nums[-2],nums[-1]
        dfs(idx,int(target))

for t in range(1,int(input())+1):
    nums,target=input().split()
    nums=list(nums)
    answer=0
    dfs(0,0)
    print(f'#{t} {answer}')
    