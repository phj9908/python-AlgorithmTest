# 오픈 채팅방(통과)
def solution(record):
    answer = []
    arr=[]
    id_arr={}
    for r in record:
        r=r.split()
        if r[1] not in id_arr.keys():
            id_arr[r[1]]=''

        if r[0]=='Enter':
            id_arr[r[1]]=r[2]
            arr.append((1,r[1]))
        elif r[0]=='Leave':
            arr.append((0,r[1]))
        else:
            id_arr[r[1]]=r[2]

    for a,b in arr:
        if a==1:
            answer.append(f'{id_arr[b]}님이 들어왔습니다.')
        else:
            answer.append(f'{id_arr[b]}님이 나갔습니다.')

    return answer