# 1983 조교의 성적매기기

tc=int(input())
list=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(1,tc+1):
    n,k=map(int,input().split())
    arr=[]
    for i in range(n):
        score=0
        a,b,c= map(int,input().split())
        score=a*0.35+b*0.45+c*0.2
        arr.append((i,score))
    arr=sorted(arr,key=lambda x:x[1],reverse=True)
    
    for i in range(len(arr)):
        if arr[i][0]==k-1:
            n//=10
            answer=list[i//n]
    print(f'#{t} {answer}')
