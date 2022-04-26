# 만들수 없는 금액( 다시풀기 )
n=int(input())
arr=list(map(int,input().split())) # 3 2 1 1 9
arr.sort()

target=1 # 만들려는 금액
for i in arr:
    if target<i: # 만들수 없는 금액을 찾았을 때
        break
    target+=i
print(target)


 