# 스택 : Last In First Out 물병의 물
# 큐 : First In First Out 샤프심의 샤프심(지우개부분에 심 넣어야 함)

# '스택에 push하는 순서는 반드시 오름차순을 지키도록 한다'
# 문제 이해: 4 3 6 수열을 만들려면 1 2 3 4 까지 push하고 / 3 4를 pop한 다음 / 5 6 push/ 6 pop -> pop한 원소들로 수열 생성

n = int(input())
count = 0
stack = []
result = []
no_message=True

for i in range(0,n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        exit(0) #a clean exit without any errors / problems

if no_message==False:
    print("NO")
else:
    print("\n".join(result))