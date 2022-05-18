# 만들수 없는 금액( 다시풀기 )
#  누적합과 화폐단위를 비교해가면서 구하기
#  화폐단위가 누적합 보다 클 경우, 그 사이에 갭이 존재한다는 뜻
# https://aeroej.tistory.com/162
n=int(input())
arr=list(map(int,input().split())) # 3 2 1 1 9
arr.sort()

target=1 # 만들려는 금액( 최소 화폐단위인 1원부터 있는지 확인)
for i in arr:
    if target<i: # 갭 발생, 만들수 없는 금액을 찾았을 때
        break
    target+=i
print(target)


 