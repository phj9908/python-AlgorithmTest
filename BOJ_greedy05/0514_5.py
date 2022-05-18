# 20300 서강근육맨
def fun(start, end):
    while start <= end:
        if start == end:
            x.append(arr[start])
            break
        else:
            x.append(arr[start] + arr[end])
            start += 1
            end -= 1
    return max(x)

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
x = []
if len(arr) % 2 == 1:
    x.append(arr.pop())
    print(fun(0, len(arr) - 1))
else:
    print(fun(0, len(arr) - 1))

