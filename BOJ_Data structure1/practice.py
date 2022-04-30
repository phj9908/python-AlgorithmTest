arr=[]
for i in range(9):
    arr.append(int(input()))
arr=sorted(arr)
s=[]

def dfs(start):
    global answer

    if len(s)==7:
        if sum(s)==100:
            for i in s:   # answer=s 해서 마지막에 출력하려 했으나 그렇게하면 answer이랑 s랑 연동되어서 answer까지 계속 바뀜
                print(i) 
            exit()
        return 
    for i in arr[start:]:
        s.append(i)
        dfs(arr.index(i)+1)
        s.pop()

dfs(0)
