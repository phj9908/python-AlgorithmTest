# 두 개 뽑아서 더하기
s = []
answer = []
def dfs(arr, visited, idx):
    if len(s) == 2:
        answer.append(sum(s))
        return
    for i in range(idx, len(arr)):
        if not visited[i]:
            visited[i] = True
            s.append(arr[i])
            dfs(arr, visited, i)
            s.pop()
            visited[i] = False

def solution(numbers):
    global answer

    visited = [False] * len(numbers)
    dfs(numbers, visited, 0)
    answer = sorted(set(answer))

    return answer