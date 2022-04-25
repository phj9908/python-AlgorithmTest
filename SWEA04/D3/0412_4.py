#4406 모음이 보이지 않는 사람

arr=['a','e','i','o','u']
tc=int(input())
for t in range(1,tc+1):
    word=list(input())
    answer=''
    for w in word:
        if w not in arr:
            answer+=w
    print(f'#{t} {answer}')