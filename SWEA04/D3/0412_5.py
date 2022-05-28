# 1215. 회문

for t in range(1,11):
    n=int(input())
    arr=[ list(input()) for _ in range(8)]
    answer=0

    for i in range(8):
        for j in range(8-n+1):
            word=arr[i][j:j+n]
            if word==word[::-1]:
                answer+=1
        for j in range(8-n+1):
            word=''
            for w in range(n):
                word+=arr[j+w][i]
            if word==word[::-1]:
                answer+=1
    
    print(f'#{t} {answer}')
