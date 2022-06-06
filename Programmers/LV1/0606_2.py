# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    strings = sorted(strings, key=lambda x: (x[n], x)) # x[n]자리 기준으로 먼저 정렬한 뒤, x[n]자리가 같다면 전체 문자열 기준으로 정렬 (["abce", "abcd", "cdx"]-> ["abcd", "abce", "cdx"]
    return strings