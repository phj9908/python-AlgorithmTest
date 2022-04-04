def solution(operation):
     
    import heapq

    min,mix=0,0
    answer=[]

    for i in operation:
        oper=i.split()
        if oper=='I':
            heapq.heappush(answer,int(oper[1]))
        elif len(answer)>0 and oper[0]=='D':
            if oper[1]=='-1':
                min=heapq.heappop(answer)
            else:
                max=answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
    if len(answer)==0:
        return [0,0]
    else:
        return [answer.pop(answer.index(heapq.nlargest(1,answer)[0])),answer.pop(answer.index(heapq.nsmallest(1,answer)[0]))]

