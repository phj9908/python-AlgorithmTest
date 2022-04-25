# 1220 Magnetic
for t in range(1,11):
    n=int(input())
    arr=[ list(input().split()) for _ in range(n)]
    
    answer=0
    for i in range(n):
        red=0  # '1'
        blue=0  # '2' 
        for j in range(n):
            if arr[j][i]=='1':
                red+=1
            elif red>=1 and arr[j][i]=='2':
                answer+=1
                red=0
    print(f'#{t} {answer}')
