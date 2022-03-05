#1874 스택수열
#https://pacific-ocean.tistory.com/231

# 스택 : Last In First Out 물병의 물
# 큐 : First In First Out 샤프심의 샤프심(지우개부분에 심 넣어야 함)

# '스택에 push하는 순서는 반드시 오름차순을 지키도록 한다'
# 문제 이해: 4 3 6 수열을 만들려면 1 2 3 4 까지 push하고 / 3 4를 pop한 다음 / 5 6 push/ 6 pop -> pop한 원소들로 수열 생성

n = int(input())
stack=[]
result=[]
cnt = 1 # 1부터 push

for _ in range(n):
    num = int(input())
    while cnt <= num : # 입력한 수를 만날 때까지 1부터 push
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
    
