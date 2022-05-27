#4396 지뢰찾기(북마크)
import sys


#n=int(input())
n=8
sys.stdin = open("input.txt", "r")

arr=[ list(sys.stdin.readline().strip()) for i in range(n)] # 지뢰배열
sys.stdin=open('input2.txt')
res_arr=[ list(sys.stdin.readline().strip()) for i in range(n)]
# res_arr=[ list(input()) for i in range(n) ] # 공백없는 문자열 여러줄 받을때 : 문자열 input()마다 list()로 감싸기(이중으로 감싸기)
d=[(-1,0),(1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
pang=False

def p():
    global arr,res_arr
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='*':
                res_arr[i][j]='*'
    return

for i in range(n):
    for j in range(n):
        if not pang and arr[i][j]=='*' and res_arr[i][j]=='x':
            p()
            pang=True
        elif arr[i][j]=='.' and res_arr[i][j]=='x':
            cnt=0
            for dir in range(8):
                ny=i+d[dir][0]
                nx=j+d[dir][1]
                if 0<=ny<n and 0<=nx<n and arr[ny][nx]=='*':
                    cnt+=1
            res_arr[i][j]=str(cnt)  # 문자열을 리스트로 입력받았다면 가능 , 그냥 [ sys.stdin.readline().strip() for i in range(n)]은 에러남

for i in res_arr:
    i=''.join(i)
    print(i)
