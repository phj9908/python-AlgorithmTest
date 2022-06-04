# 폰켓몬
def solution(nums):
    answer = len(nums)//2
    nums=set(nums)

    return min(answer,len(nums))