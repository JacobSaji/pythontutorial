def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if sum==n:
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")
num=int(input("Enter a number to check if it is an Armstrong number: "))
armstrong(num)