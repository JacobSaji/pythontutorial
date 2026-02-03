def squareroot(x):
    if x<0:
        print("Square root cannot be found for negative numbers")
        exit()
    else:
        root=x**0.5
        print(f"The square root of {x} is {root}")
num=int(input("Enter a number to find its square root: "))
squareroot(num)