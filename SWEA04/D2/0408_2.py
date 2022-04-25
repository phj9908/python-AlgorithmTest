# 1989.초심자의 회문검사(틀렸었음)
tc=int(input())
for t in range(1,tc+1):
    answer=1
    s=input()
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]: # 첫 인덱스 0 / 마지막 인덱스 -1
            answer=0
    print(f'#{t} {answer}')
   
         
     

 