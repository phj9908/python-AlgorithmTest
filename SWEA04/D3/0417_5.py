# 4676. 늘어지는 소리 만들기

tc = int(input())

for t in range(1,tc+1):
    word = list(input())
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True) # 큰 인덱스 부터 삽입해줘야 뒤섞이지 않기에!!!!
    for i in arr:
        word.insert(i,'-') # insert(인덱스,넣을 원소)

    print(f'#{t}',end=' ');print(''.join(word))  # ''.join(word)나 *word는 f''안에 표현 불가능!!!