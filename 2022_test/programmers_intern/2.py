def solution(rooms, target):
    hash = {}
    answer = []
    for r in rooms:
        arr = []
        for i in range(len(r) - 1, -1, -1):
            if r[i]==']':
                arr=list(r[i:].split(',')) # arr.append()로 했다가 [['James','Ace']]이래 됨. 결과적으로
                hash={ name:0 for name in arr}  # name=['James']가 되어 TypeError: unhashable type: 'list' 뜸
            if r[i].isdigit():
                k = 1
                while 1:
                    if r[i - k] == '[':
                        break
                    k += 1
                num = r[i:i + k]
                num = num[::-1]
                for j in arr:
                    if hash[j] != 0:
                        hash[j].append(num)
                    else:
                        hash[j] = num
    for i, v in hash.items():
        v = int(v)
        if v == target:
            continue
        answer.append((i, len(hash[i]), abs(target - v)))  # 이름, 자리갯수, 방 거리

    ans = []
    for (i, l, d) in sorted(answer, key=lambda x: x[1]):
        for ii, ll, dd in sorted(answer[i], key=lambda x: x[2]):
            ans.append(ii)

    return ans