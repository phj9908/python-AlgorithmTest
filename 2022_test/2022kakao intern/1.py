def solution(survey, choices):
    arr= {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    answer = []

    for i,v in enumerate(choices):
        if v<4:
            arr[survey[i][0]]+=v
        elif v>4:
            arr[survey[i][1]]+=v-4
        else:
            arr[survey[i][0]]+=100
            arr[survey[i][1]]+=100

    for k,v in arr.items():
        if v>0:
            answer.append(k)

    arr2=[['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(len(arr2)):
        if arr2[i][0] in answer and arr2[i][1] in answer:
            if arr[arr2[i][0]]>arr[arr2[i][1]]:
                answer.remove(arr2[i][1])
            elif arr[arr2[i][0]] < arr[arr2[i][1]]:
                answer.remove(arr2[i][0])
            else:
                arr2[i]=sorted(arr2[i])
                answer.remove(arr2[i][1])
        elif arr2[i][0] not in answer and arr2[i][1] not in answer:
            arr2[i] = sorted(arr2[i])
            answer.insert(i,arr2[i][0])

    answer=''.join(answer)
    return answer
input_arr=list(input().split())
cho=list(map(int,input().split()))
print(solution(input_arr,cho))