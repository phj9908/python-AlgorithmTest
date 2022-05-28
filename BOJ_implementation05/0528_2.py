#5766 할아버지는 유명해(다시 풀기)
while 1:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    player= [ [0,i] for i in range(10001)] # (등장횟수, 선수번호)

    for _ in range(n):
        for i in map(int,input().split()): # 입력받으면서 가중치 할당
            player[i][0]+=1 # 각 선수번호마다 등장횟수에 +1

    player=sorted(player,key=lambda x:(-x[0],x[1]))
    second_score=player[1][0]
    second_place=[player[1][1]]
    for i in range(2,10001): # 2등 선수와 점수가 같은 선수들 찾기
        if player[i][0]==second_score:
            second_place.append(player[i][1])
        else:
            break
    print(*second_place)

