# 5215. 햄버거 다이어트 (다시풀어보기)
# 앞의 2817. 부분 수열의 합의 재귀함수와 유사함.
def recur(idx,score,cal):
    global sum_score

    if cal>l:
        return
    sum_score=max(sum_score,score)

    if idx==n: #recur() 의 idx=1일 때 arr[0]의 값들이 들어가니까 idx=n일때 까지 sum하고 리턴
        return
    recur(idx+1,score+arr[idx][0],cal+arr[idx][1]) # 다음햄버거에 현재재료를 넣는 경우
    recur(idx+1,score,cal) # 재료를 넣지 않는 경우

tc=int(input())
for t in range(1,tc+1):
    n,l=map(int,input().split())
    sum_score=0
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))

    recur(0,0,0)
    print(f'#{t} {sum_score}')
 
            
            
