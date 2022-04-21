# 성적이 낮은 순서로 학생 출력하기
n=int(input())
arr=[]
for i in range(n):
    a,b=input().split()
    arr.append((a,b))
    
arr=sorted(arr,key=lambda x:int(x[1]))
for i in arr:
    print(i[0],end=' ')
