# 14467 소가 길을 건너간 이유1
def toggle(x):
    if x==0:
        return 1
    return 0

n=int(input())
arr=[ list(map(int,input().split())) for i in range(n)]
stack=[-1]*n
cnt=0
for i,a in arr:
    if stack[i-1]!=-1:
        if a==toggle(stack[i-1]):
            stack[i-1]=a
            cnt+=1
    else:
        stack[i-1]=a
print(cnt)