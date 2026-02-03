def encrypt(text,shift):
    result=''
    for i in text:
        if i.isupper():
            result+=chr((ord(i)+shift-65)%26+65)
        elif i.islower():
            result+=chr((ord(i)+shift-97)%26+97)
        else:
            result+=i
    return result
def decrypt(text,shift):
    result=''
    for i in text:
        if i.isupper():
            result+=chr((ord(i)-shift-65)%26+65)
        elif i.islower():
            result+=chr((ord(i)-shift-97)%26+97)
        else:
            result+=i
    return result

text=input("Enter the text: ")
shift=int(input("Enter the shift value: "))
choice=input("Type 'e' to encrypt or 'd' to decrypt: ")
if choice=='e':
    encrypted_text=encrypt(text,shift)
    print(f"Encrypted text: {encrypted_text}")
elif choice=='d':
    decrypted_text=decrypt(text,shift)
    print(f"Decrypted text: {decrypted_text}")
else:
    print("Invalid choice! Please type 'e' or 'd'.")