n = int(input())
ans = []

for i in range(1, n + 1):
    if i % 2 == 0:
        ans.append(2)
    else:
        ans.append(1)
if n%2!=0:
    ans[-1]=3
print(*ans)
