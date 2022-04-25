# 5162. 두가지 빵의 딜레마
tc= int(input())
for t in range(1,tc+1):
    a,b,c=map(int,input().split())
    answer=max(c//a,c//b)

    print(f'#{t} {answer}')