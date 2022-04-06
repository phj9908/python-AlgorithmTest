# 6603 로또 : 여러 숫자들 중 6개 뽑아 사전순 출력

#백트래킹ver
def dfs(start):
    if len(visited)==6:
        print(*visited)
        return 
    for i in s[start:]:
        if i in visited:
            continue
        visited.append(i)
        dfs(s.index(i))
        visited.pop()

while True:
    visited=[]
    nums= list(map(int,input().split()))
    n=nums[0]
    if n==0:
        break
    s=nums[1:] # 혹은 ==> del nums[0]

    dfs(0)
    print() # 테스트 케이스간에 한 줄 띄우기

# # combinations 활용
# from itertools import combinations # => 가능한 조합들 반환 / prmutations은 존재하는 순열들 반환

# while True:
#     nums= list(map(int,input().split()))
#     n=nums[0]
#     if n==0:
#         break
#     del nums[0]
#     nums=list(combinations(nums,6))
#     for i in nums:
#         print(*i)

#     print() # 테스트 케이스간에 한 줄 띄우기

