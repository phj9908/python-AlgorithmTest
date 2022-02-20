n = int(input())
stack=[]
result=[]
cnt = 1 # 1부터 수열 시작하니까

for _ in range(n):
    num = int(input())
    while cnt <= num : # 입력한 수를 만날 때까지 오름차순으로 push
        stack.append(cnt)
        result.append('+')
        cnt +=1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else :
        print('NO')
        break
else : # for문의 break에 끊김이 없었을 경우
    for i in result:
        print(i)
    
