#k번째 수
def solution(array, commands):
    answer = []

    for i in range(len(commands)): 
        
        # a,b,c = commands # commands[i][0]따위를 미리 변수로 생성..
        part=array[commands[i][0]-1:commands[i][1]] 
        print(part)
        part.sort()
        answer.append(part[commands[i][2]-1])
        
    return answer