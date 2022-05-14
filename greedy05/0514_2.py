# 11399 ATM
n=int(input())
t=list(map(int,input().split()))+[0]
t=sorted(t)
answer=0
for i in range(len(t)):
    answer+=sum(t[:i+1])
print(answer)
