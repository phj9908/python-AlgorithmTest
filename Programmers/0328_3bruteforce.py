# 모의고사
def solution(answers):
    answer=[]
    
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==num1[i%len(num1)]:
            score[0]+=1
        if answers[i]==num2[i%len(num2)]:
            score[1]+=1
        if answers[i]==num3[i%len(num3)]:
            score[2]+=1
            
    for i,v in enumerate(score):
        if max(score)==v:
            answer.append(i+1)
            
    return answer