# 17609 회문(이분탐색으로 안하면 시간초과,다시풀기)

def secondCheck(word,left,right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True


def firstCheck(word,left,right):
    while (left < right): # else문 가면 바로 탈출하는데 굳이 whlie 할 이유가? (나중에 수정해보기)
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            check1 = secondCheck(word,left+1,right)
            check2 = secondCheck(word,left,right-1)
            if(check1 or check2):
                return 1
            else:
                return 2
    return 0

n = int(input())
for _ in range(n):
    word = input()
    left=0
    right=len(word)-1
    ans = firstCheck(word,left,right)
    print(ans)
