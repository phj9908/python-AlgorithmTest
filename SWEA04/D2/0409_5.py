# 1974 스도투 검증(다시 풀어보기)

def check(arr): # 행,열,3x3행렬 각각 검사하면서 list에 1-9사이 중복되는 값이 할당되면 스탑하는 방식
    for i in range(9):
        
        list=[]
        for j in range(9):
            if arr[i][j] in list:
                return 0
            list.append(arr[i][j])
       	
        list=[]
        for j in range(9):
            if arr[j][i] in list:
                 return 0
            list.append(arr[j][i])
        
        for j in range(9):
            if i%3==0 and j%3==0:
                list=[]
                for row in range(3):
                    for col in range(3):
                        if arr[i+row][j+col] in list:
                            return 0
                        list.append(arr[i+row][j+col])
    return 1
    
tc=int(input())
for t in range(1,tc+1):
    arr=[list(map(int,input().split())) for i in range(9)]
    print(f'#{t}',end=' ');print(check(arr))