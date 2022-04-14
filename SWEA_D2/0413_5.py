# 5601 주스나누기
tc=int(input())
for t in range(1,tc+1):
    n=int(input())
    answer=[('1/{}'.format(n))]*n

    print(f'#{t} ');print(*answer)