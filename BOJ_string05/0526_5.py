# 1764 듣보잡
n,m=map(int,input().split())
hash={}
for i in range(n):
    name=input()
    if name in hash.keys():
        hash[name]+=1
    else:
        hash[name]=1
cnt=0
for i in range(m):
    name=input()
    if name in hash.keys():
        hash[name]-=1
        cnt+=1
    else:
        hash[name]=1

print(cnt)
for k,v in sorted(hash.items(),key=lambda x:x[0]):
    if v==0:
        print(k)

