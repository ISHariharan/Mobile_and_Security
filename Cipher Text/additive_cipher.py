str = input("Enter a word : ")
key = int(input("Enter a key : "))
length = len(str)
empty = ""
str = str.lower()


for i in str:
    if(i.isalpha()):
        temp = (ord(i) + key) % 97
        temp = temp % 26
        temp = temp + 97
        empty += chr(temp)
    else: empty += chr(ord(i) + key)

print("Encypted string : ", empty)

result = ""
for i in empty :
    if(i.isalpha()) :
        if(ord(i) - key < 97):
            div = (ord(i) - key) + 26
        else:
            div = ord(i) - key
        temp = (div) % 97
        temp = temp % 26
        temp = temp + 97
        result += chr(temp)
    else : result += chr(ord(i) - key)
    
print("Decrypted string : ", result)