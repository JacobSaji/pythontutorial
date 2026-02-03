def palcheck(s):
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')
def symcheck(s):
    length=len(s)
    mid=length//2

    if length%2!=0:
        print(f'"{s}" is not a symmetric string.')
        exit()

    first_half=s[:mid]
    second_half=s[mid:]
    if first_half == second_half:
        print(f'"{s}" is a symmetric string.')
    else:
        print(f'"{s}" is not a symmetric string.')
string = input("Enter a string to check for palindrome: ")
palcheck(string)
symcheck(string)