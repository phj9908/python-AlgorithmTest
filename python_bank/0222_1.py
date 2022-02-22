n , m =map(int,input().split())
nums = list(map(int,input().split()))

result=0

for i in range(n):
    sum=nums[i]
    if sum != m :
        for j in range(i+1,n):
            sum +=nums[j]
            if sum == m :
                result+=1
    else :
        result +=1

print(result)
