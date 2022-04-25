# 5549. 홀수일까 짝수일까
tc=int(input())
even_arr=['0','2','4','6','8']
for t in range(1,tc+1):
    n=input()
    if n[-1] in even_arr:
        answer='Even'
    else:
        answer='Odd'
    
    print(f'#{t} {answer}')