# 2578 빙고
from collections import deque

def check():
    global answer
    dir = [(1, 1), (1, -1)]
    bingo = 0

    for i in range(5):
        if my_arr[i] == [0] * 5:
            bingo += 1
            if bingo >= 3:
                return True

        cnt = 0
        for j in range(5):
            if my_arr[j][i] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1
            if bingo >= 3:
                return True

        if i == 0:
            y, x = i, 0
            cnt = 0
            while 0 <= y < 5 and 0 <= x < 5:
                if my_arr[y][x] == 0:
                    cnt += 1
                y += dir[0][0]
                x += dir[0][1]
            if cnt == 5:
                bingo += 1
                if bingo >= 3:
                    return True
            y, x = i, 4
            cnt = 0
            while 0 <= y < 5 and 0 <= x < 5:
                if my_arr[y][x] == 0:
                    cnt += 1
                y += dir[1][0]
                x += dir[1][1]
            if cnt == 5:
                bingo += 1
                if bingo >= 3:
                    return True

    return False

answer = 0
my_arr = []
for i in range(5):
    my_arr.append(list(map(int, input().split())))
r_arr = []
for i in range(5):
    r_arr.append(list(map(int, input().split())))
r_arr = sum(r_arr, [])  # 2차원 리스트를 1차원 리스트로
r_arr = deque(r_arr)

while r_arr:
    x=r_arr.popleft()
    answer+=1
    for i in range(5):
        if x in my_arr[i]:
            for j in range(5):
                if my_arr[i][j] == x:
                    my_arr[i][j]=0
                    if check():
                        print(answer)
                        exit()
