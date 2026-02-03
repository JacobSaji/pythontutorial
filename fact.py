def fact(n):
    if n<0:
        print("Factorial cannot be found for negative numbers")
        exit()
    else:
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
        
num=int(input("Enter a number to find its factorial: "))
result=fact(num)
print(result)