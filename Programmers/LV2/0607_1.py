# 문자열 압축( LV2는 다 다시풀기 ... )
def solution(s):
    answer = []
    for step in range(1, len(s) // 2 + 1):
        prev = s[:step]
        word = ''
        cnt = 1
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                cnt += 1
            else:
                if cnt >= 2:
                    word += str(cnt) + prev
                else:
                    word += prev
                cnt = 1
                prev = s[i:i + step]
        if cnt >= 2:
            word += str(cnt) + prev
        else:
            word += prev
        answer.append(len(word))

    if not answer: # 입력 문자열 길이가 1일 때
        return 1

    return min(answer)
