#h-인덱스
#h-인덱스 란? https://www.ibric.org/myboard/read.php?Board=news&id=270333
#위에선 1부터 시작하지만 문제에선 인용횟수가 0회이상부터임.인덱스0부터 해야함

def solution(citations):
    citations.sort(reverse=True)
    for idx,c in enumerate(citations):
        if c<=idx:
            return idx
        return len(citations)

        