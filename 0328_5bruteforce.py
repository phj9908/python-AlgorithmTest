# 카펫
def solution(brown, yellow):
    total=brown+yellow # 48
    num=[]
    for i in range(3,int((total)**0.5+1)): 
        if total%i==0:
            num.append(sorted([i,total/i],reverse=True)) ([8,6],[12,4])
            #print(num)
    for col,row in num:
        if yellow==(col-2)*(row-2):
            return [col,row]


