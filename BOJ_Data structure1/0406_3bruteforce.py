# 1759 암호만들기
# 주어진 m개의 알파벳 중에 최소 모음(a,e,i,o,u) 1개를 가진 n개의 골라 사전순으로 출력 (abc(O) ,bac (X))
# 아스키 코드) a:97, e:101, i:105, o:111, u:117

n,m=map(int,input().split())
s=sorted(list(map(ord,input().split())))
b_asc=set(range(98,123)) #  자음 아스키코드
a_asc=set([97,101,105,111,117]) # 모음 아스키 코드
b_asc-=a_asc
visited=[]

def dfs(start):
    if len(visited)==n:
        check_a=False
        check_b=0
        for i in visited:
            if i in a_asc: 
                check_a=True
            elif i in b_asc:  # 그냥 else 해도 됨
                check_b+=1
            if check_a and check_b>=2: # 모음이 적어도 하나 있고 자음이 2개 이상이면
                print(''.join(map(str,map(chr,visited))))
                return

    for i in s[start:]:
        if i not in visited:
            visited.append(i)
            dfs(s.index(i))
            visited.pop()
dfs(0)

# # combinations 활용ver
# from itertools import combinations

# n,m = map(int,input().split())
# chars=sorted(input().split())
# a_asc=set(['a','e','i','o','u'])

# for char in list(combinations(chars,n)):
#     check_a,check_b=0,0
#     for c in char:
#         if c in a_asc:
#             check_a+=1
#         else:
#             check_b+=1
#     if check_a >0 and check_b >=2:
#         print(''.join(char))
    

