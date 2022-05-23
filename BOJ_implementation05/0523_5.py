# 20291 파일정리
n=int(input())
hash={}
for i in range(n):
    a,b=input().split('.')
    if b in hash.keys():
        hash[b]+=1
    else:
        hash[b]=1
for k,v in sorted(hash.items(),key=lambda x:x[0]): # 해시의 key기준으로 오름차순 정렬
    print(f'{k} {v}')

