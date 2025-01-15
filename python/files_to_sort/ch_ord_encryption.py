toBeEncrypted = input("Please type your message to be encrypted here \n >>>")
encryptedMessage = ''
key = int(input("Please type the key you wish to use here \n >>>"))

for each in toBeEncrypted:
    newLetter = ord(each) + key
    encryptedMessage += chr (newLetter)

print(encryptedMessage)
