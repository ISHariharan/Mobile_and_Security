str = input("Enter a word : ")
key = int(input("Enter a key : "))
length = len(str)
empty = ""
# print(ord('a'))
# print(ord('z'))
for i in str:
    temp = (ord(i) + key) % 97
    temp = temp % 26
    temp = temp + 97
    empty += chr(temp)

print("Encypted string : ", empty)

str = ""
for i in empty :
    if(ord(i) - key < 97):
        div = (ord(i) - key) + 26
    else:
        div = ord(i) - key
    temp = (div) % 97
    temp = temp % 26
    temp = temp + 97
    str += chr(temp)
    
print("Decrypted string : ", str)