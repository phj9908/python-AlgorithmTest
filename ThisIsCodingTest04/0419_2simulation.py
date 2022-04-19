# 시각 
n=int(input())

dst=((n+1)*3600)-1
src=0
answer=0

while src<dst:
    src+=1
    h=str(src//3600)
    m=str((src%3600)//60)
    s=str((src%3600)%60)

    if ('3' in h) or ('3' in m) or ('3'in s):
        answer+=1
print(answer)

    