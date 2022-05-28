# 3809. 화섭이의 정수 나열 (다시 풀어보기)
tc=int(input())
for t in range(1,tc+1):
    n=int(input())

    # 입력받는 수 문자열 하나로 만들기 (방법1)
    # arr=list(in.txt().split()) ['9','5','3']
    # arr=''.join(arr) '953'

    #                            (방법2)
    word=''
    while 1:
        word+=''.join(input().split()) # 입력이 한줄이거나 여러줄일수도 있기에 while로 받고 
        if len(word)==n:               # n자리 채우면 입력 끝
            break

    count=0
    answer=0
    while 1:
        if str(count) not in word:
            answer=count
            break
        count+=1
    print(f'#{t} {answer}')

