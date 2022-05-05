# 2817. 부분 수열의 합 https://serendipity24.tistory.com/112 그림 참고
# 재귀함수로 부분집합 만들기(combinations는 시간초과 되었다.)
# https://velog.io/@tks7205/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B6%80%EB%B6%84%EC%A7%91%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0 재귀함수로 부분집함 만들기 코드참고
# # 다시 풀어보기

def recur(subset, i):
  global cnt

  if i == n: 		     
    return

  subset.append(arr[i])
  if sum(subset)==k:
      cnt+=1

  recur(subset, i+1) 	     # i번째 원소가 '있을' 때의 경우에서 분화

  subset.pop()
  recur(subset, i+1)	     # i번째 원소가 '없을' 때의 경우에서 분화

tc=int(input())
for t in range(1,tc+1):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    cnt=0

    recur([],0)
    print(f'#{t} {cnt}')


 