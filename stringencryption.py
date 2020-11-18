#lab 6 week 4: messing w strings

def getDoubleAlphabet(alphabet):
    dAlphabet = alphabet + alphabet
    return dAlphabet

#Implementing a simple caesar cipher

def getMessage():
    stringToEncrypt = input("Enter a string to encrypt")
    return stringToEncrypt

def getCyperKey():
    cipherKey = input("Enter a number to use as a cipher")
    return cipherKey

def encryptMessage(message, cipherKey, alphabet):
    #encrypts a function using an integer cypher

    encryptedMessage = ""
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    #runs an encryptMessage in the opposite direction, lol
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


def runCaesarCipherProgram():
    #neat lil user interaction

    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
