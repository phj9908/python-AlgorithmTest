# 10804. 문자열의 거울상
tc= int(input())
arr={'b':'d','d':'b','p':'q','q':'p'}

for t in range(1,tc+1):
    word=input()
    answer=''
    for i in word[::-1]:
        answer+=arr[i]
    print(f'#{t} {answer}')