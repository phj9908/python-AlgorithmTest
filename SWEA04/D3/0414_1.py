#1213. [S/W 문제해결 기본] 3일차 - String
for t in range(1,11):
    tc=int(input())
    word=input()
    str=input()

    length=len(word)
    answer=0
    for i in range(len(str)):

        if str[i:i+length]==word :
            answer+=1
    print(f'#{t} {answer}')