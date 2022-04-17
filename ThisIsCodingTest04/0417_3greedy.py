# 곱하기 혹은 더하기
n=input()
n_arr=[int(i) for i in n]
answer=0
for i in range(1,len(n_arr)):
    if n_arr[i]<=1 or answer <=1:
        answer+=n_arr[i]
    else:
        answer*=n_arr[i]

print(answer)