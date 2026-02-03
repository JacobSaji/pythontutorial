str1=input("Enter first string: ")
str2=input("Enter second string: ")

result = str1+str2
print("Concatenated string is:", result)

start=int(input("Enter starting index for substring: "))
end=int(input("Enter ending index for substring: "))
substring = result[start:end]
print("Substring is:", substring)