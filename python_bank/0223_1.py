n=int(input())

def prime_fun(n):
    sieve=[True]*n

    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(2*i,n,i): # i이후 i배수들은 false
                sieve[j]=False
    result = [i for i in range(2,n) if sieve[i] == True]
    return result

print(len(prime_fun(n)))
