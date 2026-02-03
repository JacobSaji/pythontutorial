def dec(binary):
    decimal=0
    binary=str(binary)
    length=len(binary)
    for i in range(length):
        bit=int(binary[length-i-1])
        decimal+=bit*(2**i)
    return decimal
num=int(input("Enter a binary number to convert to decimal: "))
result=dec(num)
print(f"The decimal equivalent of binary {num} is {result}")