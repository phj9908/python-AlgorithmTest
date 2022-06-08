# 타겟넘버
answer=0
def dfs(numbers,target,cnt, total):
    global answer

    if cnt==len(numbers):
        if total==target:
            answer+=1
        return

    dfs(numbers,target, cnt + 1, total+numbers[cnt])
    dfs(numbers,target,cnt + 1, total-numbers[cnt])

def solution(numbers, target):
    dfs(numbers,target,0,0)
    return answer


