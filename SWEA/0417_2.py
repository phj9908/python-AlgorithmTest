# 1221. [S/W 문제해결 기본] 5일차 - GNS
tc=int(input())
hash={'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7,'EGT':8,'NIN':9}
hash__={0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}

for t in range(1,tc+1):
    str,n=input().split()
    n=int(n)
    word=list(input().split())
    answer=[]
    for i in range(len(word)):
        answer.append(hash[word[i]])
    answer=sorted(answer)
    
    for i in range(len(answer)):
        answer[i]=hash__[answer[i]]
    print(f'#{t}')
    print(*answer)

