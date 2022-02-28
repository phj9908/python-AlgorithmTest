#1463 : 1로 만들기(-1, //2, //3의 방법. 그러나 x로 2의 배수가 나올지 3의 배수가 나올지 아무의 배수가 아닌수가 나올지 모르기에 3가지 경우에 모두 대비한 코드 작성)
# 메모이제이션 기법 이용: 리스트를 만들어 한번 연산한 걸 저장해서 다음에 그 연산을 할때 저장된걸 가져다 쓰는 방법. 동일한 계산의 반복을 피할 수 있다.
# x=10일 때, -1의 경우 10-1=9, 또 9가 1이되는 최소횟수= (9가 1이되는  최소횟수) +1(10에서 1을 뺀 연산)
#          , 2로 나눠 질 때의 경우 10//2 = 5 , 또 5가 1이 되는 횟수 = (5가 1이되는 횟수) +1(10에서 2나눈 연산)
# https://kangmin1012.tistory.com/34

x=int(input())
dp=[0,0,1,1] # 인덱스 값(0,1,2,3)에 해당하는 1로 만들기 연산 횟수 (최소수) 미리 저장, 4부터는  그 횟수가 1을 넘어서 미리 저장x

for i in range(4,x+1):
    dp.append(dp[i-1]+1) # -1 해서 1로 만드는 경우
    if i%2==0 : # 2로 나눠질 경우
        dp[i] = min(dp[i],dp[i//2]+1) # -1로 1 만드는 경우 연산 횟수와 2로 나눠질때 1로 만드는 경우 중 더 작은 횟수 도출
    if i%3==0 :
        dp[i] = min(dp[i],dp[i//3]+1) #                               3 

print(dp[-1])