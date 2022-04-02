#14500 테트로미노 , dfs 기초문제 풀어보고 dfs풀이도 이해하기,,
# dfs 풀이:  https://oranz.tistory.com/7
# 브루트포스로만 푼 풀이 https://wisdom-990629.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-14500%EB%B2%88-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8

n,m=map(int,input().split()) # 세로 X 가로
arr= []
for i in range(n):
    arr.append(list(map(int,input().split())))
 
max=0
case = [    # 기본, 대칭, 회전 다 포함한 테트로미노 좌표 정보 ,총 19가지
    # case 1
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # case 2
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # case 3
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # case 4
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # case 5
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [-1, 1], [0, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
]

def check(sum):
    global max
    if sum > max:
        max=sum

def tetromino(i,j):
    for x in range(19):
        sum=0
        for y in range(4):
            try:    
                sum+= arr[i+case[x][y][0]][j+case[x][y][1]]
            except:# 인덱스 아웃 에러가 발생할수도 있음
                break
        check(sum)
        
for i in range(n):
    for j in range(m):
        tetromino(i,j)

print(max)
            
