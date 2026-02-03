def primenum(lower,upper):
    primes=[]
    for num in range(lower,upper+1):
        if num>1:
            is_prime=True
            for i in range(2,num):
                if(num%i)==0:
                    is_prime=False
                    break
            if is_prime:
                primes.append(num)
    return primes
lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
result=primenum(lower,upper)
print(f"Prime numbers between {lower} and {upper} are: {result}")