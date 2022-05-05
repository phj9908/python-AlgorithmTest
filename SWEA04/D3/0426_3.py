# 4522. 세상의 모든 팰린드롬
tc=int(input())
for t in range(1,tc+1):
    word=input()
    answer='Exist'

    for i in range(len(word)//2):
        if word[i]==word[-i-1] or word[i]=='?' or word[-i-1]=='?': #  ex) adda a?ca ab?a
            continue
        answer='Not exist'


    print(f'#{t} {answer}')