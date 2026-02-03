def fibanocci(n):
    stor=[0,1]
    if n<=0:
        print("Fibonacci cannot be found for non-positive numbers")
        exit()
    elif n==1:
        print(stor[0])
    elif n==2:
        print(stor[0],stor[1])
    else:
        for i in range(2,n):
            next=stor[i-1]+stor[i-2]
            stor.append(next)
        print("Fibonacci series is: ")
        for j in stor:
            print(j,end=" ")

num=int(input("Enter a number to find its Fibonacci series: "))
fibanocci(num)