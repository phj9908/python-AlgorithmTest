# 15650 n과m(2) : 이전 조건+ 고른 수열은 오름차순이어야 함


n,m = map(int,input().split())
s=[]
def dfs():
    if len(s)==m:
        for i in range(m-1):
            if s[i]>s[i+1]: # 오름차순 아니면 나가기
                return
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()    
dfs()

# 다른 풀이 (더 빠름)
# def dfs(start):
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(start,n+1): # 무조건 시작 숫자보다 큰숫자와 조합
#         if i in s:
#             continue
#         s.append(i)
#         dfs(i)
#         s.pop()    
# dfs(1)