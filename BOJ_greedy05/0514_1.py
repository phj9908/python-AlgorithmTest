# 1758 알바생 강호
n=int(input())
tip=[]
for i in range(n):
    tip.append(int(input()))
tip=sorted(tip,reverse=True)
answer=0
for i in range(len(tip)):
    x=tip[i]-((i+1)-1)
    if x<0:
        break
    answer+=x
print(answer)